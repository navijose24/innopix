from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models



class AdminUser(AbstractUser):
    # Add related_name arguments to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="adminuser_set",  # Change related_name to avoid conflict
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="adminuser_set",  # Change related_name to avoid conflict
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    # Add any additional fields or methods for AdminUser here


class ClientUser(models.Model):
    """Client logs in with phone number only."""

    phone_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number
