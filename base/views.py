from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registered successfully.")
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Or another page
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def task(request):
    return render(request, 'task/list.html')

def board(request):
    return render(request, 'task/board.html')

def details(request):
    return render(request, 'task/details.html')

def timeline(request):
    return render(request, 'timeline/timeline.html')

def profile(request):
    return render(request, 'profile/profile.html')

def auth_registration(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('auth_registration')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('auth_registration')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registered successfully. Please log in.")
        return redirect('auth_login')

    return render(request, 'authunticate/auth_registration.html')

def auth_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # or any page you want to redirect after login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('auth_login')

    return render(request, 'profile/profile.html') 
def abc(request):
    return render("")

