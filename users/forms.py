from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile  # Ensure Profile is defined in your models.py

# Use the custom or default User model
User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # This dynamically uses the correct User model
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User  # Ensure consistency with the custom User model
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile  # Ensure Profile exists in users/models.py
        fields = ['image']
