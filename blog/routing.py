from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/chat/global/", consumers.GlobalChatConsumer.as_asgi()),
    path("ws/chat/post/<slug:slug>/", consumers.PostChatConsumer.as_asgi()),
]
