from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', user_views.home, name='home'), 
    path('', include('users.urls')),  # Include URLs from the `users` app
]
