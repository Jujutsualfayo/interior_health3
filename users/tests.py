from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class LoginTests(TestCase):
    
    def setUp(self):
        # Create a test user for the login test
        self.client.login(username='testuser', password='testpassword')
    
    def test_login_invalid_user(self):
        # Test login with invalid credentials
        url = reverse('users:login')
        data = {'username': 'invaliduser', 'password': 'wrongpassword'}
        
        response = self.client.post(url, data)
        
        # Check if the error message appears in the response
        self.assertContains(response, "Invalid username or password.")
    
    def test_login_valid_user(self):
        # Test login with valid credentials
        url = reverse('users:login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        
        response = self.client.post(url, data)
        
        # Check if the user is redirected to the home page after login
        self.assertRedirects(response, reverse('users:home'))
        
    def test_login_view_get(self):
        # Test if the GET request loads the login page properly
        response = self.client.get(reverse('users:login'))
        
        # Check if the login page is rendered (status code 200)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
