from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

app_name = 'users'

# Create a router and register the UserViewSet
router = DefaultRouter()
router.register(r'api/users', views.UserViewSet, basename='user')

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
    # API routes
    path('', include(router.urls)), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]
