from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model



class UsersAppTests(TestCase):
    def setUp(self):
        # Create a test user group (e.g., "Patient")
        self.group = Group.objects.create(name="Patient")

        # Create a test user using the custom User model
        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password123"
        )
        self.user.groups.add(self.group)

        # Initialize the test client
        self.client = Client()

    def test_home_page(self):
        """Test the home page loads successfully."""
        # Make sure the 'users:home' URL is defined in your app's urls.py
        response = self.client.get(reverse('users:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_user_registration(self):
        """Test user registration form submission."""
        User = get_user_model()
        response = self.client.post(reverse('users:register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'complex_password123',
            'password2': 'complex_password123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        """Test logging in with valid credentials."""
        response = self.client.post(reverse('users:login'), {
            'username': 'testuser',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login

    def test_invalid_login(self):
        """Test logging in with invalid credentials."""
        response = self.client.post(reverse('users:login'), {
            'username': 'wronguser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)  # Stays on the login page
        self.assertContains(response, 'Invalid username or password.')

    def test_user_logout(self):
        """Test user logout."""
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout

    def test_profile_access(self):
        """Test accessing the profile page requires login."""
        # Test without login
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

        # Test with login
        self.client.login(username="testuser", password="password123")
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')
