from django.shortcuts import render,redirect
# Create your views here.

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        # Validation
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('user_register_link')
        
        # Create user
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password1)
        user.save()
        messages.success(request, "Account created successfully.")
        return redirect('user_login_link')

    return render(request, 'register.html')




def user_login(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('user_home_link')  # Replace 'home' with your desired redirect path
        else:
            messages.error(request, "Invalid credentials.")
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('user_login_link')

def user_home(request):
    a = request.user
    return render(request,'home.html',{'user':a})