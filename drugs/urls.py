from django.urls import path
from . import views
from .views import drug_list_api, drug_detail_api, drug_list_view

app_name = 'drugs'

urlpatterns = [
    path('api/drugs/', drug_list_api, name='drug_list_api'),  # List and create drugs
    path('api/drugs/<int:pk>/', drug_detail_api, name='drug_detail_api'),  # Retrieve, update, delete a single drug
    path('drugs/', drug_list_view, name='drug_list'), 
    path('place_order/<int:drug_id>/', views.place_order_with_drug, name='place_order_with_drug'),
]
