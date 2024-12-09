from django.shortcuts import render
from .models import Drug

def drug_list(request):
    drugs = Drug.objects.all()  # Fetch all drugs
    return render(request, 'drugs/drug_list.html', {'drugs': drugs})
