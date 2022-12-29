from django.shortcuts import render, redirect

from products.models import Product, Category
from orders.models import Order, OrderItem
from users.models import User

# Update and Read Orders

def orders(request):
    orders = Order.objects.all()
    return render(request, 'admin/orders.html', {'orders':orders})

def update_order(request):
    return render(request, 'admin/update_order.html', {'orders':orders})



# Delete and Read Users

def users(request):
    return render(request, 'admin/users.html')

def delete_users(request):
    pass


# Read Update Delete Products (create in products.views.py)

def products(request):
    return render(request, 'admin/products.html')

def update_product(request):
    return render(request, 'admin/update_product.html')

def delete_product(request):
    pass


# CRUD Categorys

def categorys(request):
    return render(request, 'admin/categorys.html')

def create_category(request):
    return render(request, 'admin/create_category.html')

def update_category(request):
    return render(request, 'admin/update_category.html')

def delete_category(request):
    pass