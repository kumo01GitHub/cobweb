"""Custom user model."""
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import validate_slug, MinLengthValidator
from django.db import models


class CustomUserManager(BaseUserManager):
    """Custom user manager."""

    def create_user(self, username, password=None):
        """Create user."""
        if not username:
            raise ValueError("Users must have a user name")

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """Create superuser."""
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    """Custom user model."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Metadata for custom user model."""
        verbose_name = "user"

    username = models.CharField(
        verbose_name = "user name",
        max_length = 32,
        validators = [
            validate_slug,
            MinLengthValidator(4)
        ],
        unique = True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return str(self.username)

    def has_perm(self, perm, obj=None):  # pylint: disable=unused-argument
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):  # pylint: disable=unused-argument
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
