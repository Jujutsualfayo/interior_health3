from django import forms
from .models import Order
from drugs.models import Drug

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['drug', 'quantity']

    # Optionally, you can dynamically generate the list of available drugs
    drugs = forms.ModelChoiceField(queryset=Drug.objects.all(), widget=forms.Select)
    quantity = forms.IntegerField(min_value=1)
