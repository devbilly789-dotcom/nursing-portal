from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Authentication
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),

    # Student payment & dashboard
    path("payment/", views.payment_view, name="payment"),
    path("waiting/", views.waiting_view, name="waiting"),
    path("dashboard/", views.dashboard_view, name="dashboard"),

    # Admin approval
    path("approve_students/", views.approve_students, name="approve_students"),

    # PayHero callback
    path("callback/", views.payhero_callback, name="payhero_callback"),
]
