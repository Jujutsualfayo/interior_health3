from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render  # For rendering the global home page
from django.conf import settings
from django.conf.urls.static import static

# View for rendering the global home.html
def global_home(request):
    return render(request, 'home.html')

urlpatterns = [
    # Root URL for the global home page
    path('', global_home, name='global_home'),

    # Admin panel URL
    path('admin/', admin.site.urls),

    # Users app URLs
    path('users/', include('users.urls')),

    # Drugs app URLs
    path('drugs/', include('drugs.urls')),

    # Orders app URLs
    path('orders/', include('orders.urls')),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
