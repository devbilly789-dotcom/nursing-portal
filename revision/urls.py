from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("payment/", views.payment_view, name="payment"),
    path("waiting/", views.waiting_view, name="waiting"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("approve_students/", views.approve_students, name="approve_students"),
    path("callback/", views.payhero_callback, name="payhero_callback"),
]
