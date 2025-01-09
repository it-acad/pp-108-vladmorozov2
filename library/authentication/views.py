# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt


# Registration view
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("last_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not first_name or not last_name or not email or not password:
            return HttpResponse("All fields are required!", status=400)

        if CustomUser.get_by_email(email):
            return HttpResponse("User with this email already exists!", status=400)

        user = CustomUser.create(
            email=email,
            password=password,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
        )

        if user:
            return redirect("login")
        return HttpResponse("Failed to create user!", status=500)

    return render(request, "authentication/register.html")


# Login view
def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = CustomUser.get_by_email(email=email)
        if user and user.password == password:
            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, user)  # Логін
            return redirect("home")
        return HttpResponse("Invalid credentials!", status=401)

    return render(request, "authentication/login.html")


# Logout view
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")
    return HttpResponse("User not logged in!", status=400)


def home(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "authentication/home.html")
