# views.py
from django.shortcuts import render, redirect
from .models import Drug
from .forms import DrugForm  # Import the DrugForm

# View to display the list of drugs and handle drug addition
def drug_list(request):
    if request.method == 'POST':
        form = DrugForm(request.POST, request.FILES)  # Handle the form submission (including file uploads)
        if form.is_valid():
            form.save()  # Save the new drug
            return redirect('drug_list')  # Redirect to the same page after successful submission
    else:
        form = DrugForm()  # Display an empty form when the page is loaded
    
    drugs = Drug.objects.all()  # Fetch all drugs from the database
    return render(request, 'drugs/drug_list.html', {'drugs': drugs, 'form': form})  # Pass both the drug list and form to the template
