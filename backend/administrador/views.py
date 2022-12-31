from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.core.validators import validate_email

from products.models import Product, Category
from orders.models import Order, OrderItem
from users.models import User
from . forms import  CategoryForm, NewsletterForm
from products.forms import ProductForm
from . utilities import send_news, news_letter_create
from . models import Newsletter


# Hacer como en utils.py con Json
def newsletter(request):
    content=request.POST['content']

    news = news_letter_create(request, content=content)

    send_news(news)
    messages.success(request, 'Emails Send!')
    return redirect('news_form')


def news_form(request):
    return render(request, 'admin/newsletter.html')







def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)

        if not email:
            messages.error(request, "You must type legit email to subscribe to a Newsletter")
            return redirect("/")

        subscribe_user = Newsletter.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))  

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = Newsletter()
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))  





@staff_member_required(login_url='home')
def orders(request):
    orders = OrderItem.objects.all()
    return render(request, 'admin/orders.html', {'orders':orders})



def check(request, order_id):
    order = OrderItem.objects.get(pk=order_id)
    order.is_paid = 'paid'
    order.save()
    messages.success(request, 'Producto Eliminado!')
    return redirect('orders')

def not_check(request, order_id):
    order = OrderItem.objects.get(pk=order_id)
    order.is_paid = ''
    order.save()
    messages.success(request, 'Producto Eliminado!')
    return redirect('orders')

    
    



# Delete and Read Users
@staff_member_required(login_url='home')
def users(request):
    users = User.objects.all()

    return render(request, 'admin/users.html', {'users':users})

@staff_member_required(login_url='home')
def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    messages.success(request, ('user Eliminado!'))
    return redirect('users')

# Read Update Delete Products (create in products.views.py)

@staff_member_required(login_url='home')
def products(request):
    products = Product.objects.all()

    return render(request, 'admin/products.html', {'products':products})

@staff_member_required(login_url='home')
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

@staff_member_required(login_url='home')
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    messages.success(request, 'Producto Eliminado!')
    return redirect('products')


# CRUD Categorys
@staff_member_required(login_url='home')
def categorys(request):
    categorys = Category.objects.all()
    return render(request, 'admin/categorys.html', {'categorys': categorys})

@staff_member_required(login_url='home')
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

@staff_member_required(login_url='home')
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

@staff_member_required(login_url='home')
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    messages.success(request, 'Producto Eliminado!')
    return redirect('categorys')
