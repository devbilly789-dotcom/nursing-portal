from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Register page (homepage)
    path('', views.register_view, name='register'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Payment system
    path('payment/', views.payment_view, name='payment'),
    path('waiting/', views.waiting_view, name='waiting'),

    # Student dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Admin approval page
    path('approve/', views.approve_students, name='approve_students'),
]