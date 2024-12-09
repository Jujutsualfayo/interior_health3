# drugs/forms.py
from django import forms
from .models import Drug

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name', 'category', 'description', 'manufacturer', 'expiry_date', 'price', 'stock_quantity', 'minimum_stock']
