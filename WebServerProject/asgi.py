import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path
import WebServerApp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebServerProject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            WebServerApp.routing.websocket_urlpatterns
        )
    ),
})
