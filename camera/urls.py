from django.urls import path, include
from camera.views import index

urlpatterns = [
    path('', index),
]
