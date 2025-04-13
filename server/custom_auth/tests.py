"""Tests for custom authentication."""

from django.test import TestCase
from custom_auth.models import CustomUser

class CustomUserModelTests(TestCase):
    """Tests for CustomUser model."""

    def setUp(self):
        """Set up test environment."""
        self.user = CustomUser.objects.create_user(
            username="testuser",
            password="testpassword"
        )

    def test_user_creation(self):
        """Test user creation."""
        self.assertEqual(self.user.username, "testuser")
        self.assertTrue(self.user.check_password("testpassword"))
        self.assertFalse(self.user.is_admin)
        self.assertTrue(self.user.is_active)

    def test_superuser_creation(self):
        """Test superuser creation."""
        superuser = CustomUser.objects.create_superuser(
            username="admin",
            password="adminpassword"
        )
        self.assertEqual(superuser.username, "admin")
        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.check_password("adminpassword"))

    def test_user_str(self):
        """Test user string representation."""
        self.assertEqual(str(self.user), "testuser")
