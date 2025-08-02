from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        UserName = request.POST.get("UserName")
        password = request.POST.get("password")
        # print(email, password)
        user = authenticate(request, username=UserName, password=password)
        if user is not None:
            messages.success(request, "Login successful!")
            return render(request, "accounts/home.html")  # Redirect to home or dashboard
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "accounts/login.html")
    return render(request, 'accounts/login.html')

def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
           messages.error(request, "Passwords do not match")
           return render(request, "accounts/register.html")

        # ✅ Check for existing username
        if User.objects.filter(username=name).exists():
            messages.error(request, "Username already exists")
            return render(request, "accounts/register.html")

        # ✅ Check for existing email (optional)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, "accounts/register.html")

        myuser = User.objects.create_user(username=name, email=email, password=password1)
        myuser.save()
        messages.success(request, "Account created successfully!")
        return render(request, "accounts/login.html")

    return render(request, "accounts/register.html")

