from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    # Role-Based Dashboards
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('health-worker/dashboard/', views.health_worker_dashboard, name='health_worker_dashboard'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
]
