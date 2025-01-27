from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from .models import Drug
from orders.models import Order

class DrugListViewTest(TestCase):
    def setUp(self):
        # Create a user for login
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Create admin user for testing "Place Order" visibility for admins
        self.admin_user = User.objects.create_user(username='adminuser', password='password123', is_staff=True)
        
        # Create patient user and add to 'Patients' group
        self.patient_user = User.objects.create_user(username='patientuser', password='password123')
        patients_group, created = Group.objects.get_or_create(name='Patients')
        self.patient_user.groups.add(patients_group)
        
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
        
        # Check if the "Place Order" button is NOT visible for a normal user
        self.assertNotContains(response, 'Place Order')

    def test_place_order_button_for_patient(self):
        # Log in as a patient
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
        self.client.login(username='patientuser', password='password123')
        
        # Get the "Place Order" button for the drug
        response = self.client.get(reverse('orders:place_order_with_drug', args=[self.drug1.id]))
        
        # Check if the redirect is correct (this should be the order placement page)
        self.assertEqual(response.status_code, 302)  # Check if it's a redirect
        # Use the correct order detail page URL
        self.assertRedirects(response, reverse('orders:order_detail', args=[self.drug1.id]))

    def test_redirect_to_home_for_non_patient(self):
        # Log in as a non-patient user (testuser)
        self.client.login(username='testuser', password='password123')
        
        # Attempt to access the "Place Order" page for a drug
        response = self.client.get(reverse('orders:place_order_with_drug', args=[self.drug1.id]))
        
        # Check if the response is a redirect to the home page (as they are not a patient)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_place_order_button_not_visible_for_non_patient_and_non_admin(self):
        # Log in as a normal user (not admin or patient)
        self.client.login(username='testuser', password='password123')
        
        # Access the drug list view
        response = self.client.get(reverse('drugs:drug_list'))
        
        # Ensure that the "Place Order" button is NOT visible for a non-patient/non-admin user
        self.assertNotContains(response, 'Place Order')
