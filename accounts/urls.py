from django.urls import path
from .views import ClientRegisterView, RegisterChoiceView, TherapistRegisterView, dashboard_view
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path("register/", RegisterChoiceView.as_view(), name="register"),
    path("register/client/", ClientRegisterView.as_view(), name="register_client"),
    path("register/therapist/", TherapistRegisterView.as_view(), name="register_therapist"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
]
