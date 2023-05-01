from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class AppUserManager(BaseUserManager):
    """
    Create a new user with the given email and password.

    Args:
        email (str): The email address of the user.
        password (str, optional): The password to use for the new user. If not
            provided, a random password will be generated.

    Raises:
        ValueError: If `email` or `password` are not provided.

    Returns:
        User: The newly created user object.
    """

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('An email is required')
        if not password:
            raise ValueError('A password is required')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        """
    Create a superuser with the given email and password.

    Args:
        email (str): The email address of the superuser.
        password (str, optional): The password for the superuser. Defaults to None.

    Raises:
        ValueError: If email or password are not provided.

    Returns:
        User: The newly created superuser object.
    """
        if not email:
            raise ValueError('An email is required')
        if not password:
            raise ValueError('A password is required')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()
        return user


class AppUser(AbstractUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, max_length=50)
    username = models.CharField(max_length=50, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AppUserManager()

    def __str__(self):
        return self.username
