from django.shortcuts import render

def my_orders(request):
    return reender(request, 'orders/my_orders.html')

def my_sales(request):
    return render(request, 'orders/my_sales.html')