from django.contrib import admin
from django.urls import path, include
from users import views as user_views  # Import views from the users app

urlpatterns = [
    path('', global_home, name='global_home'),  # Root URL for the global home page
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('drugs/', include('drugs.urls')),
    path('orders/', include('orders.urls')),  
]
