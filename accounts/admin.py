from django.contrib import admin
from .models import User, ClientProfile, TherapistProfile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "is_staff")

@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "age", "emergency_contact")

@admin.register(TherapistProfile)
class TherapistProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "license_number", "specialty", "rating")
