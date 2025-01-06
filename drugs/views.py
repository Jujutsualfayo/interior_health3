from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Drug
from .serializers import DrugSerializer

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
