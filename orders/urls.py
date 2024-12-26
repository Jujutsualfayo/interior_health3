from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('list/', views.order_list, name='order_list'),
    path('place/', views.place_order, name='place_order'),  # For general order placement
    path('place/<int:drug_id>/', views.place_order, name='place_order_with_drug'),  # For order placement with a specific drug
    path('<int:pk>/', views.order_detail, name='order_detail'),
    path('<int:pk>/cancel/', views.cancel_order, name='cancel_order'),
]
