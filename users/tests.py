from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile

class UserTests(TestCase):
    def setUp(self):
        """Create a user for testing."""
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword123'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)
        self.user.save()

    def test_register_user(self):
        """Test the user registration form."""
        url = reverse('users:register')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        }
        response = self.client.post(url, data)
        
        # Ensure the user is redirected to the home page after successful registration
        self.assertRedirects(response, reverse('users:home'))
        
        # Verify the user exists in the database
        user = get_user_model().objects.get(username='newuser')
        self.assertEqual(user.email, 'newuser@example.com')

    def test_login_user(self):
        """Test user login functionality."""
        url = reverse('users:login')
        data = {
            'username': self.user.username,
            'password': self.user_data['password'],
        }
        response = self.client.post(url, data)
        
        # Ensure the user is redirected to the home page after logging in
        self.assertRedirects(response, reverse('users:home'))
        
    def test_login_invalid_user(self):
        """Test invalid user login."""
        url = reverse('users:login')
        data = {
            'username': 'invaliduser',
            'password': 'wrongpassword',
        }
        response = self.client.post(url, data)
        
        # Check if the login form re-renders with an error message
        self.assertContains(response, 'Invalid username or password.')

    def test_logout_user(self):
        """Test the logout functionality."""
        self.client.login(username=self.user.username, password=self.user_data['password'])
        url = reverse('users:logout')
        response = self.client.get(url)
        
        # Ensure the user is redirected to the login page after logging out
        self.assertRedirects(response, reverse('users:login'))
        
    def test_profile_update(self):
        """Test the profile update functionality."""
        self.client.login(username=self.user.username, password=self.user_data['password'])
        
        # Data to update the profile
        updated_data = {
            'username': 'updateduser',
            'email': 'updateduser@example.com',
        }
        
        url = reverse('users:profile')
        response = self.client.post(url, updated_data)
        
        # Ensure the profile is updated successfully
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.email, 'updateduser@example.com')
        
    def test_profile_picture_upload(self):
        """Test the profile picture upload functionality."""
        self.client.login(username=self.user.username, password=self.user_data['password'])
        
        # Prepare a dummy image file for upload
        with open('path/to/test/image.jpg', 'rb') as img:
            image_file = SimpleUploadedFile('image.jpg', img.read(), content_type='image/jpeg')
        
        url = reverse('users:profile')
        response = self.client.post(url, {
            'image': image_file
        })
        
        # Ensure that the image file was uploaded correctly
        self.user.profile.refresh_from_db()
        self.assertTrue(self.user.profile.image.name.endswith('image.jpg'))
        
    def test_register_form_invalid(self):
        """Test the user registration form with invalid data."""
        url = reverse('users:register')
        data = {
            'username': '',
            'email': 'invalidemail.com',
            'password1': 'short',
            'password2': 'short',
        }
        response = self.client.post(url, data)
        
        # Check for form errors
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        self.assertFormError(response, 'form', 'password1', 'This password is too short.')

    def test_message_on_profile_update(self):
        """Test that the correct message appears when updating profile."""
        self.client.login(username=self.user.username, password=self.user_data['password'])
        
        # Simulate profile update
        updated_data = {
            'username': 'newname',
            'email': 'newname@example.com',
        }
        
        url = reverse('users:profile')
        response = self.client.post(url, updated_data)
        
        # Check if success message is shown
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(str(messages[0]) == "Your profile has been updated!")

