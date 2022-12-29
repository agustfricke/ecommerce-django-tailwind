from django.shortcuts import render
import json
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from products.cart import Cart
from . utilities import checkout, notificar_vendedor, notificar_cliente

@login_required
def order(request):
    cart = Cart(request)

    data = json.loads(request.body)

    total = cart.get_total_price()


    order = checkout(request, 
            customer = request.user,
            name = data['form']['name'],
            last_name = data['form']['last_name'],
            email = request.user.email,
            address = data['form']['address'],
            zip_code = data['form']['zip_code'],
            city = data['form']['city'],
            mobile = data['form']['mobile'],
            total = float(data['form']['total']))

    cart.clean()

    notificar_cliente(order)
    notificar_vendedor(order)
    messages.success(request, 'order Completada!')

    return JsonResponse('Pago completado!', safe=False)

