from django.urls import path
from .views import *

urlpatterns = [
    path('', encode),
    path('decode/<str:code>/', decode, name='decode'),
]
