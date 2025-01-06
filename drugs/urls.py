# drugs/urls.py
from django.urls import path
from .views import drug_list_api

app_name = 'drugs'

urlpatterns = [
    path('api/drugs/', drug_list_api, name='drug_list_api'),
]
