from django.contrib import admin
from django.urls import path, include
from users import views as user_views  # Import views from the users app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),  # Global home view
    path('users/', include('users.urls')),
    path('drugs/', include('drugs.urls')),
    path('orders/', include('orders.urls')),  
    
]
