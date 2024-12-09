# drugs/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Drug
from .forms import DrugForm
from django.utils import timezone
from datetime import timedelta

class DrugModelTest(TestCase):
    """Test the Drug model."""

    def setUp(self):
        """Create a sample drug for testing."""
        self.drug = Drug.objects.create(
            name="Test Drug",
            category="Antibiotic",
            description="A powerful antibiotic",
            manufacturer="Pharma Corp.",
            expiry_date=timezone.now() + timedelta(days=30),
            price=100.00,
            stock_quantity=5,
            minimum_stock=10
        )

    def test_is_low_stock(self):
        """Test if the drug is low on stock."""
        self.assertTrue(self.drug.is_low_stock())

    def test_is_not_low_stock(self):
        """Test if the drug is not low on stock."""
        self.drug.stock_quantity = 15
        self.drug.save()
        self.assertFalse(self.drug.is_low_stock())

class DrugFormTest(TestCase):
    """Test the DrugForm form."""

    def test_form_valid(self):
        """Test if the form is valid with correct data."""
        form_data = {
            'name': 'Test Drug',
            'category': 'Antibiotic',
            'description': 'A powerful antibiotic',
            'manufacturer': 'Pharma Corp.',
            'expiry_date': '2025-12-31',
            'price': 100.00,
            'stock_quantity': 50,
            'minimum_stock': 10
        }
        form = DrugForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        """Test if the form is invalid with missing required fields."""
        form_data = {'name': '', 'category': 'Antibiotic'}
        form = DrugForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # 'name' field is required

class DrugViewTest(TestCase):
    """Test the views in the drugs app."""

    def setUp(self):
        """Create a sample drug."""
        self.drug = Drug.objects.create(
            name="Test Drug",
            category="Antibiotic",
            description="A powerful antibiotic",
            manufacturer="Pharma Corp.",
            expiry_date="2025-12-31",
            price=100.00,
            stock_quantity=50,
            minimum_stock=10
        )

    def test_drug_list_view(self):
        """Test if the drug list view is rendering correctly."""
        response = self.client.get(reverse('drug_list'))  # URL pattern name should match the view
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Drug")  # Ensure that the drug name is in the response
        self.assertTemplateUsed(response, 'drugs/drug_list.html')  # Check if the correct template is used

    def test_drug_list_empty(self):
        """Test if the drug list view handles empty drug list correctly."""
        # Delete all drugs
        Drug.objects.all().delete()
        response = self.client.get(reverse('drug_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No drugs available.")  # Check if the appropriate message is shown
