from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import ClientRegisterForm, TherapistRegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

class ClientRegisterView(CreateView):
    form_class = ClientRegisterForm
    template_name = "accounts/register_client.html"
    success_url = reverse_lazy("core:home")


class TherapistRegisterView(CreateView):
    form_class = TherapistRegisterForm
    template_name = "accounts/register_therapist.html"
    success_url = reverse_lazy("login")

class RegisterChoiceView(TemplateView):
    template_name = "accounts/register_choice.html"

@login_required
def dashboard_view(request):
    user = request.user

    if hasattr(user, "client_profile"):
        return render(request, "accounts/client_dashboard.html", {"user": user})
    elif hasattr(user, "therapist_profile"):
        return render(request, "accounts/therapist_dashboard.html", {"user": user})
    else:
        return redirect("accounts:register")
