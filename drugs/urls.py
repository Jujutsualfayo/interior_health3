# drugs/urls.py
from django.urls import path
from . import views

app_name = 'drugs'  # 

urlpatterns = [
    path('list/', views.drug_list, name='drug_list'),
]
