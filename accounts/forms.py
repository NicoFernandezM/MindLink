from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ClientProfile, TherapistProfile

class ClientRegisterForm(UserCreationForm):
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    country = forms.CharField(required=False)
    province = forms.CharField(required=False)
    street = forms.CharField(required=False)
    phone_number = forms.CharField(required=False)
    emergency_contact_name = forms.CharField(required=False)
    emergency_contact_phone = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit)
        ClientProfile.objects.create(
            user=user,
            date_of_birth=self.cleaned_data["date_of_birth"],
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data.get("last_name"),
            country=self.cleaned_data.get("country"),
            province=self.cleaned_data.get("province"),
            street=self.cleaned_data.get("street"),
            phone_number=self.cleaned_data.get("phone_number"),
            emergency_contact_name=self.cleaned_data.get("emergency_contact_name"),
            emergency_contact_phone=self.cleaned_data.get("emergency_contact_phone"),
        )
        return user

class TherapistRegisterForm(UserCreationForm):
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    license_number = forms.CharField(required=True)
    specialty = forms.CharField(required=True)
    country = forms.CharField(required=True)
    province = forms.CharField(required=True)
    street = forms.CharField(required=False)
    phone_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit)
        TherapistProfile.objects.create(
            user=user,
            date_of_birth=self.cleaned_data["date_of_birth"],
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data.get("last_name"),
            license_number=self.cleaned_data["license_number"],
            specialty=self.cleaned_data["specialty"],
            country=self.cleaned_data["country"],
            province=self.cleaned_data["province"],
            street=self.cleaned_data.get("street"),
            phone_number=self.cleaned_data.get("phone_number"),
        )
        return user