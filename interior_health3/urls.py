from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render  # For rendering the global home page
from django.conf import settings
from django.conf.urls.static import static

def global_home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', global_home, name='global_home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('drugs/', include('drugs.urls')),  
    path('orders/', include('orders.urls')),  

    # API routes
    path('api/drugs/', include('drugs.urls')),  # Assuming your drugs app has API views
    path('api/orders/', include('orders.urls')),  # This will include the API endpoints for orders
    path('api/users/', include('users.urls')),  # Assuming your users app has API views
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
