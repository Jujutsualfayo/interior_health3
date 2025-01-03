from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from .models import Drug
from .forms import DrugForm 

# View to display the list of drugs and handle drug addition
@login_required 
def drug_list(request):
    if request.method == 'POST':
        form = DrugForm(request.POST, request.FILES)  # Handle the form submission (including file uploads)
        if form.is_valid():
            form.save()  # Save the new drug
            return redirect('drugs:drug_list')  # Redirect to the same page after successful submission
    else:
        form = DrugForm()  # Display an empty form when the page is loaded
    
    # Fetch all drugs from the database, even if none exist
    drugs = Drug.objects.all()
    
    # Pass both the drug list and form to the template, ensuring drugs is never None
    return render(request, 'drugs/drug_list.html', {'drugs': drugs, 'form': form})
