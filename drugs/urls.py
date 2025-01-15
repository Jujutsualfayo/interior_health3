from django.urls import path
from .views import drug_list_api, drug_detail_api, drug_list_view

app_name = 'drugs'

urlpatterns = [
    path('api/drugs/', drug_list_api, name='drug_list_api'),  # List and create drugs
    path('api/drugs/<int:pk>/', drug_detail_api, name='drug_detail_api'),  # Retrieve, update, delete a single drug
    path('drugs/', drug_list_view, name='drug_list'),  # Web view for the list of drugs
]
