from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('place_order/<int:drug_id>/', views.place_order, name='place_order'),
]
