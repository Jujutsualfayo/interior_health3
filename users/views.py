from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

# Home view
def home(request):
    return render(request, 'users/home.html')  # Rendering the home.html template for the homepage

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assign default group or role
            group = Group.objects.get(name='Patient')  # Ensure this group exists in your DB
            user.groups.add(group)
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

# User login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the homepage after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

# User logout view
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

# Profile view
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile.html', context)

# Role-specific dashboard view
@login_required
def dashboard(request):
    if request.user.role == 'admin':
        return render(request, 'users/admin_dashboard.html')
    elif request.user.role == 'health_worker':
        return render(request, 'users/health_worker_dashboard.html')
    elif request.user.role == 'patient':
        return render(request, 'users/patient_dashboard.html')
    else:
        return HttpResponse('Role not recognized.')
