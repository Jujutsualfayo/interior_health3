from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('order/list/', views.order_list, name='order_list'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
    path('<int:pk>/cancel/', views.cancel_order, name='cancel_order'),
    path('place/<int:drug_id>/', views.place_order, name='place_order'),
]

