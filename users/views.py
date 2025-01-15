from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import Group, User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Traditional views remain unchanged

def home(request):
    return render(request, 'home.html')

def register(request):
    """
    Handles user registration and assigns the appropriate group based on their role.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assign group based on role
            try:
                if user.role == 'admin':
                    group = Group.objects.get(name='Admin')
                elif user.role == 'health_worker':
                    group = Group.objects.get(name='Health Worker')
                elif user.role == 'patient':
                    group = Group.objects.get(name='Patient')
                else:
                    group = None

                if group:
                    group.user_set.add(user)
                else:
                    messages.error(request, 'Invalid role assigned to the user.')

            except Group.DoesNotExist:
                messages.error(request, 'Role group does not exist. Contact admin.')

            login(request, user)
            return redirect('users:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    """
    Handles user login.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('users:home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'users/login.html')

def logout_view(request):
    """
    Logs out the user and redirects them to the login page.
    """
    logout(request)
    return redirect('users:login')

@login_required
def profile(request):
    """
    Handles user profile updates and ensures a profile exists for the logged-in user.
    """
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('users:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Admin').exists())
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Health Worker').exists())
def health_worker_dashboard(request):
    return render(request, 'health_worker_dashboard.html')

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Patient').exists())
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

# API Views
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def current_user(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
