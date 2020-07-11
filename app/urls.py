from django.urls import path
from .views import *

urlpatterns = [
    path('', encode),
    path('<str:code>/', decode),
]
