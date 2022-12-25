from django.shortcuts import render

def login_page(request):
    return render(request, 'users/login.html')

def register_page(request):
    return render(request, 'users/register.html')

def my_profile(request):
    return render(request, 'users/my_profile.html')

def vendor_profile(request):
    return render(request, 'users/vendor_profile.html')

def become_vendor(request):
    return render(request, 'users/become_vendor.html')

