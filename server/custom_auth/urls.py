"""Custom authentication URLs."""

from django.urls import path
from . import views

urlpatterns = [
    path('token/', views.CustomAuthToken.as_view())
]
