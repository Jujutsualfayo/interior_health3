# drugs/forms.py
from django import forms
from .models import Drug

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name', 'description', 'price', 'quantity', 'image']
