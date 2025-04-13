"""Custom authentication."""
from django.apps import AppConfig


class CustomAuthConfig(AppConfig):
    """Custom authentication app configuration."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_auth'
    verbose_name = "auth"
