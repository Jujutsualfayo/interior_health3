import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from drugs.consumers import DrugConsumer  # Update with the correct import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interior_health3.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handles HTTP requests
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/drugs/', DrugConsumer.as_asgi()),  # The WebSocket URL pattern
        ])
    ),
})
