from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'user/user_login.html')


@login_required(login_url='user_login')
def userDashboard(request):
    return render(request, 'user/user_dashboard.html')


def userLogout(request):
    logout(request)
    return redirect('user_login')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User

def userRegister(request):
    if request.method == 'POST':
        username = request.POST.get('name')  # Corrected: use this as Django username
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        # Basic validation
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'user/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'user/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'user/register.html')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        
        # Optional: Store mobile/address if you extend User model later
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect('user_dashboard')

    return render(request, 'user/register.html')



def user(request):
    return HttpResponse("User Page")
