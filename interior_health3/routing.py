# interior_health3/routing.py

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import drugs.routing
import orders.routing  # Import orders routing
import users.routing  # Import users routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            drugs.routing.websocket_urlpatterns +
            orders.routing.websocket_urlpatterns +  
            users.routing.websocket_urlpatterns  
        )
    ),
})

