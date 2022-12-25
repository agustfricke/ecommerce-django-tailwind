from django.shortcuts import render

def home(request):
    return render(request, 'products/home.html')

def product(request):
    return render(request, 'products/product.html')

def cart(request):
    return render(request, 'products/cart.html')

