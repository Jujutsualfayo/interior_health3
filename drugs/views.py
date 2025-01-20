from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Drug
from .models import Order, Drug
from .serializers import DrugSerializer


def place_order_with_drug(request, drug_id):
    # Get the drug
    drug = Drug.objects.get(id=drug_id)
    
    # Create the order (make sure you're saving the order in the database)
    order = Order.objects.create(drug=drug, user=request.user)

    # Redirect to the order detail page after the order is placed
    return redirect('orders:order_detail', order_id=order.id)

# API view to handle the list of drugs and drug creation
@api_view(['GET', 'POST'])
def drug_list_api(request):
    if request.method == 'GET':
        drugs = Drug.objects.all()
        serializer = DrugSerializer(drugs, many=True)
        return Response(serializer.data)  # Return the list of drugs in JSON format

    elif request.method == 'POST':
        serializer = DrugSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new drug
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API view to handle getting, updating, and deleting a single drug
@api_view(['GET', 'PUT', 'DELETE'])
def drug_detail_api(request, pk):
    try:
        drug = Drug.objects.get(pk=pk)
    except Drug.DoesNotExist:
        return Response({'error': 'Drug not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrugSerializer(drug)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrugSerializer(drug, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# View to render the drug list in HTML
def drug_list_view(request):
    drugs = Drug.objects.all()
    is_admin = request.user.is_staff
    is_patient = request.user.groups.filter(name='Patients').exists()

    # Debug print statements to log user and their roles
    print(f"User: {request.user}")
    print(f"Is Admin: {is_admin}")
    print(f"Is Patient: {is_patient}")

    return render(request, 'drugs/drug_list.html', {'drugs': drugs, 'is_admin': is_admin, 'is_patient': is_patient})
