from .consumers import CustomEventConsumer
from django.urls import path
urlpatterns = [
    path('', CustomEventConsumer.as_asgi())
]