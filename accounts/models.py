from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        unique=False
    )
    email = models.EmailField(
        unique=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client_profile")
    age = models.PositiveIntegerField(null=True, blank=True)
    emergency_contact = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Client: {self.user.username}"


class TherapistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="therapist_profile")
    license_number = models.CharField(max_length=50)
    specialty = models.CharField(max_length=100, null=True, blank=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"Therapist: {self.user.username}"
