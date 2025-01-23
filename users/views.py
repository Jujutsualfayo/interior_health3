from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Profile
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .serializers import UserSerializer

# Traditional views
def home(request):
    return render(request, 'home.html')

def register(request):
    """
    Handles user registration and assigns the appropriate group based on their role.
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            # Assign user to the correct group based on role
            try:
                role_group_mapping = {
                    'admin': 'Admin',
                    'health_worker': 'Health Worker',
                    'patient': 'Patient'
                }
                group_name = role_group_mapping.get(user.role, None)
                if group_name:
                    group = Group.objects.get(name=group_name)
                    group.user_set.add(user)
                else:
                    messages.error(request, 'Invalid role selected.')

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('users:home')
        else:
            messages.error(request, 'Invalid username or password.')
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
    user = request.user

    # Ensure the user has a profile
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('users:profile')
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=user.profile)

    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

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
        """
        Custom action to return the currently authenticated user's data.
        """
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
