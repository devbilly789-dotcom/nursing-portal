from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from . import views

# Root redirect
def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')  # redirect guests to login

urlpatterns = [
    path("", root_redirect, name="root"),
    path("register/", views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("payment/", views.payment_view, name="payment"),
    path("waiting/", views.waiting_view, name="waiting"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("approve_students/", views.approve_students, name="approve_students"),
    path("callback/", views.payhero_callback, name="payhero_callback"),
]
