from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.drug_list, name='drug_list'),
]
