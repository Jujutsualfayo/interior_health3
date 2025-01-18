from django.urls import path
from . import consumers  # Import the consumers from the current app

# Define the WebSocket URL patterns
websocket_urlpatterns = [
    path('ws/orders/', consumers.MyConsumer.as_asgi()),  # Map the WebSocket URL to the MyConsumer class
]
