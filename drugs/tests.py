from django.test import TestCase
from django.urls import reverse
from users.models import User  # Assuming your custom User model is here
from .models import Drug
from orders.models import Order  # Assuming you have an Order model in the 'orders' app

class DrugListViewTest(TestCase):
    def setUp(self):
        # Create a user for login
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Create admin user for testing "Place Order" visibility for admins
        self.admin_user = User.objects.create_user(username='adminuser', password='password123', is_staff=True)
        
        # Create some drugs for testing
        self.drug1 = Drug.objects.create(name='Aspirin', price=5.99, stock_quantity=50)
        self.drug2 = Drug.objects.create(name='Ibuprofen', price=7.99, stock_quantity=30)

    def test_drug_list_view(self):
        # Log in the user
        self.client.login(username='testuser', password='password123')
        
        # Access the drug list view
        response = self.client.get(reverse('drugs:drug_list'))
        
        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check if the drugs are displayed on the page
        self.assertContains(response, 'Aspirin')
        self.assertContains(response, 'Ibuprofen')
        
        # Check if the "Place Order" button is visible for the user
        self.assertContains(response, 'Place Order')

    def test_place_order_button_for_patient(self):
        # Log in as a patient
        patient_user = User.objects.create_user(username='patientuser', password='password123')
        self.client.login(username='patientuser', password='password123')
        
        # Access the drug list view
        response = self.client.get(reverse('drugs:drug_list'))
        
        # Check if the "Place Order" button is visible for the patient
        self.assertContains(response, 'Place Order')

    def test_place_order_button_for_admin(self):
        # Log in as an admin user
        self.client.login(username='adminuser', password='password123')
        
        # Access the drug list view
        response = self.client.get(reverse('drugs:drug_list'))
        
        # Check if the "Place Order" button is visible for the admin
        self.assertContains(response, 'Place Order')

    def test_redirect_to_place_order_page(self):
        # Log in as a patient user
        patient_user = User.objects.create_user(username='patientuser', password='password123')
        self.client.login(username='patientuser', password='password123')
        
        # Get the "Place Order" button for the drug
        response = self.client.get(reverse('orders:place_order_with_drug', args=[self.drug1.id]))
        
        # Check if the redirect is correct (this should be the order placement page)
        self.assertEqual(response.status_code, 200)  # Assuming the order form loads successfully

    def test_place_order_button_not_visible_for_other_users(self):
        # Log in as a normal user (not admin or patient)
        self.client.login(username='testuser', password='password123')
        
        # Access the drug list view
        response = self.client.get(reverse('drugs:drug_list'))
        
        # Ensure that the "Place Order" button is NOT visible for a non-patient/non-admin user
        self.assertNotContains(response, 'Place Order')
