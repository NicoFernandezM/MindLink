from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ClientProfile, TherapistProfile

class ClientRegisterForm(UserCreationForm):
    age = forms.IntegerField(required=False)
    emergency_contact = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")

    def clean_username(self):
        # No hacer validación de unicidad en username
        return self.cleaned_data["username"]

    def save(self, commit=True):
        user = super().save(commit)
        ClientProfile.objects.create(
            user=user,
            age=self.cleaned_data.get("age"),
            emergency_contact=self.cleaned_data.get("emergency_contact")
        )
        return user


class TherapistRegisterForm(UserCreationForm):
    license_number = forms.CharField(required=True)
    specialty = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")

    def clean_username(self):
        return self.cleaned_data["username"]

    def save(self, commit=True):
        user = super().save(commit)
        TherapistProfile.objects.create(
            user=user,
            license_number=self.cleaned_data.get("license_number"),
            specialty=self.cleaned_data.get("specialty"),
        )
        return user