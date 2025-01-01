from django.test import TestCase
from django.urls import reverse
from users.models import User

class UserRegistrationTest(TestCase):
    def test_registration_view(self):
        response = self.client.post(reverse('users:register'), {
            'username': 'testuser',
            'password1': 'password123',
            'password2': 'password123',
            'email': 'testuser@example.com',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(User.objects.filter(username='testuser').exists())
