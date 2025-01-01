from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Drug

class DrugListViewTest(TestCase):
    def setUp(self):
        # Create a user for login
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Create some drugs for testing
        Drug.objects.create(name='Aspirin', price=5.99, stock_quantity=50)
        Drug.objects.create(name='Ibuprofen', price=7.99, stock_quantity=30)

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
