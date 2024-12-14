from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

# Home view
def home(request):
    return render(request, 'users/home.html')

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group, created = Group.objects.get_or_create(name='Patient')
            user.groups.add(group)
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('users:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

# User login view
def user_login(request):
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

# User logout view
def user_logout(request):
    logout(request)
    return redirect('users:login')

# Profile view
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('users:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

# Dashboard view
@login_required
def dashboard(request):
    if request.user.groups.filter(name='Admin').exists():
        return render(request, 'users/admin_dashboard.html')
    elif request.user.groups.filter(name='Health Worker').exists():
        return render(request, 'users/health_worker_dashboard.html')
    elif request.user.groups.filter(name='Patient').exists():
        return render(request, 'users/patient_dashboard.html')
    else:
        return HttpResponse('Role not recognized.')

