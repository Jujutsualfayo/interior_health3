from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'orders'

# Create a router and register the OrderViewSet
router = DefaultRouter()
router.register(r'api/orders', views.OrderViewSet, basename='order')

urlpatterns = [
    path('list/', views.order_list, name='order_list'),
    path('place/', views.place_order, name='place_order'),  # General order placement
    path('place/drug/<int:drug_id>/', views.place_order, name='place_order_with_drug'),  # Specific drug order
    path('<int:pk>/', views.order_detail, name='order_detail'),
    path('history/', views.order_history, name='order_history'),
    path('<int:pk>/cancel/', views.cancel_order, name='cancel_order'),
    
    # Include the API routes
    path('', include(router.urls)),
]

