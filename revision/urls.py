from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('payment/', views.payment_view, name='payment'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]