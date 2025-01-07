from django.urls import path
from .views import drug_list_api, drug_list_view

app_name = 'drugs'

urlpatterns = [
    path('api/drugs/', drug_list_api, name='drug_list_api'),
    path('drugs/', drug_list_view, name='drug_list'),  # New URL for the web view
]
