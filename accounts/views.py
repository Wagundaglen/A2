# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if not username or not password1 or not password2:
            messages.error(request, 'This field is required')
            return render(request, 'accounts/register.html')

        if password1 != password2:
            messages.error(request, "The two password fields didn't match")
            return render(request, 'accounts/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'A user with that username already exists')
            return render(request, 'accounts/register.html')

        if len(password1) < 8:
            messages.error(request, 'This password is too short. It must contain at least 8 characters')
            return render(request, 'accounts/register.html')

        if email and '@' not in email:
            messages.error(request, 'Enter a valid email address')
            return render(request, 'accounts/register.html')

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        Profile.objects.create(user=user)  # Create an empty profile for the new user
        return redirect('/accounts/login/')
    else:
        return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/accounts/profile/view/')
        else:
            messages.error(request, 'Username or password is invalid')
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)  # Get the user's profile
    return render(request, 'accounts/profile_view.html', {'profile': profile})

@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)  # Get the user's profile
    if request.method == 'POST':
        profile.phone_number = request.POST.get('phone_number')
        profile.address = request.POST.get('address')
        profile.city = request.POST.get('city')
        profile.country = request.POST.get('country')
        profile.postal_code = request.POST.get('postal_code')
        profile.save()
        return redirect('/accounts/profile/view/')
    return render(request, 'accounts/profile_edit.html', {'profile': profile})







