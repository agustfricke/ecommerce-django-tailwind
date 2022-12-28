from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator


from . models import Product, Category
from . forms import ProductForm


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user
            product.slug = slugify(product.name)
            product.save()

            return redirect('my_profile')
    
    else:
        form = ProductForm()
    
    return render(request, 'products/create.html', {'form':form})

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'products/search.html', {'products':products, 'query':query})


def category(request, slug):
    categorys = get_object_or_404(Category, slug=slug)
    return render(request, 'products/category.html', {'categorys':categorys})

def home(request):
    last = Product.objects.all()[0:3]
    products = Product.objects.all()

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/home.html', {'page_obj':page_obj, 'last':last})

def product(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product.html', {'product':product})

def cart(request):
    return render(request, 'products/cart.html')

