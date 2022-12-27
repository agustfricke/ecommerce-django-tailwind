from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from . forms import RegisterUserForm
from . models import User

def logout_user(request):
    logout(request)
    messages.success(request, 'See you later!')
    return redirect('home')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)

        except:
            messages.success(request, 'User does not exist!')

        user = authenticate(request, email = email, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome ' + user.username)
            return redirect('home')

        else:
            messages.success(request, 'Username or password does not match!')
    return render(request, 'users/login.html')



def register_page(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, 'Account created!')
            return redirect('home')
        else:
            messages.success(request, 'An error occurred during registation!')

    return render(request, 'users/register.html', {'form': form})



def my_profile(request):
    return render(request, 'users/my_profile.html')

def vendor_profile(request):
    return render(request, 'users/vendor_profile.html')

def become_vendor(request):
    return render(request, 'users/become_vendor.html')

