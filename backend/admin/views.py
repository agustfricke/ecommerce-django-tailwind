from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.text import slugify

from products.models import Product, Category
from orders.models import Order, OrderItem
from users.models import User
from . forms import UpdateOrderItem, CategoryForm
from products.forms import ProductForm

# Update and Read Orders



def orders(request):
    orders = OrderItem.objects.all()
    return render(request, 'admin/orders.html', {'orders':orders})

def update_order(request, pk):
    order = OrderItem.objects.get(pk=pk)

    if request.method == 'POST':
        form = UpdateOrderItem(request.POST, instance=order)

        if form.is_valid():
            form.save()
            messages.success(request, 'Updated!')
            return redirect('orders')

    else:
        form = UpdateOrderItem(instance=order)

    return render(request, 'admin/update_order.html', {'form':form})
    



# Delete and Read Users

def users(request):
    users = User.objects.all()

    return render(request, 'admin/users.html', {'users':users})

def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    messages.success(request, ('user Eliminado!'))
    return redirect('users')

# Read Update Delete Products (create in products.views.py)

def products(request):
    products = Product.objects.all()

    return render(request, 'admin/products.html', {'products':products})

def update_product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, ('Producto Actualizado!'))
            return redirect('products')

    else:
        form = ProductForm(instance=product)

    return render(request, 'admin/update_product.html', {'form':form})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    messages.success(request, 'Producto Eliminado!')
    return redirect('products')


# CRUD Categorys

def categorys(request):
    categorys = Category.objects.all()
    return render(request, 'admin/categorys.html', {'categorys': categorys})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.slug = slugify(category.name)
            category.save()

            return redirect('categorys')
    
    else:
        form = CategoryForm()
    return render(request, 'admin/create_category.html', {'form':form})

def update_category(request, pk):
    category = Category.objects.get(pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            messages.success(request, ('category Actualizado!'))
            return redirect('categorys')

    else:
        form = CategoryForm(instance=category)
    return render(request, 'admin/update_category.html', {'form':form})

def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    messages.success(request, 'Producto Eliminado!')
    return redirect('categorys')
