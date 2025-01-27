from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from drugs.models import Drug
from django.contrib.auth.models import User
from orders.models import Order


class OrderTests(TestCase):
    def setUp(self):
        # Create a user instance
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

        # Create a test drug
        self.drug = Drug.objects.create(
            name='Test Drug',
            category='Painkillers',
            description='Effective for pain relief',
            manufacturer='Health Inc.',
            expiry_date='2025-12-31',
            price=15.50,
            stock_quantity=50
        )

        # Log in the test user (password should match the one set for the user)
        self.client.login(username='testuser', password='testpassword')
        self.user.save()

        # Create a test order
        self.order = Order.objects.create(
            user=self.user,
            drug=self.drug,
            quantity=2,
            status='Pending'  # Capitalized status
        )

    # Model Tests
    def test_order_creation(self):
        """Test that the Order model correctly creates an order."""
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.drug, self.drug)
        self.assertEqual(self.order.quantity, 2)
        self.assertAlmostEqual(self.order.total_price, 31.00, places=2)
        self.assertEqual(self.order.status, 'Pending')

    def test_order_str_representation(self):
        """Test the string representation of the Order model."""
        expected_str = f"Order #{self.order.id} by {self.user.username}"
        self.assertEqual(str(self.order), expected_str)

    # View Tests
    def test_order_list_view(self):
        """Test the order list view displays correctly."""
        response = self.client.get(reverse('orders:order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_list.html')
        self.assertContains(response, f"Order #{self.order.id}")  # Ensure order details appear
        self.assertContains(response, 'Test Drug')  # Ensure drug name appears

    def test_place_order_with_drug_view(self):
        """Test placing an order through the place order view with drug ID."""
        response = self.client.post(
            reverse('orders:place_order_with_drug', args=[self.drug.id]),
            {'quantity': 3}
        )
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertEqual(Order.objects.count(), 2)  # New order should be created
        new_order = Order.objects.last()
        self.assertEqual(new_order.quantity, 3)
        self.assertAlmostEqual(new_order.total_price, 46.50, places=2)

    def test_place_order_without_drug_view(self):
        """Test placing an order through the general place order view."""
        response = self.client.post(
            reverse('orders:place_order'),
            {'drug': self.drug.id, 'quantity': 4}
        )
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertEqual(Order.objects.count(), 2)  # New order should be created
        new_order = Order.objects.last()
        self.assertEqual(new_order.quantity, 4)
        self.assertAlmostEqual(new_order.total_price, 62.00, places=2)

    def test_place_order_insufficient_stock(self):
        """Test placing an order when stock is insufficient."""
        response = self.client.post(
            reverse('orders:place_order_with_drug', args=[self.drug.id]),
            {'quantity': 100}  # Exceeds available stock
        )
        self.assertEqual(response.status_code, 200)  # Stay on the same page
        self.assertContains(response, 'Insufficient stock.')

    def test_place_order_invalid_quantity(self):
        """Test placing an order with invalid quantity."""
        response = self.client.post(
            reverse('orders:place_order_with_drug', args=[self.drug.id]),
            {'quantity': 0}  # Invalid quantity
        )
        self.assertEqual(response.status_code, 200)  # Stay on the same page
        self.assertContains(response, 'Quantity must be greater than 0.')

    def test_order_detail_view(self):
        """Test the order detail view displays correctly."""
        response = self.client.get(reverse('orders:order_detail', args=[self.order.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_detail.html')
        self.assertContains(response, 'Test Drug')

    def test_order_list_view_empty(self):
        """Test the order list view when there are no orders."""
        Order.objects.all().delete()  # Remove all orders
        response = self.client.get(reverse('orders:order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No orders available.')

    def test_cancel_order_view(self):
        """Test the cancel order functionality."""
        initial_stock = self.drug.stock_quantity

        # Cancel the order
        response = self.client.post(reverse('orders:cancel_order', args=[self.order.id]))

        # Reload the order and drug after canceling
        self.order.refresh_from_db()
        self.drug.refresh_from_db()

        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertEqual(self.order.status, 'CANCELED')  # Status should be updated
        self.assertEqual(self.drug.stock_quantity, initial_stock)  # Stock should remain unchanged

    def test_order_history_view(self):
        """Test the order history view."""
        response = self.client.get(reverse('orders:order_history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_history.html')
        self.assertContains(response, f"Order #{self.order.id}")
