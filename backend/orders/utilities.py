from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Order, OrderItem
from products.cart import Cart


def checkout(request, customer, name, last_name, email, address, zip_code, city, mobile, total):
    order = orden.objects.create(
                                    customer=customer,
                                    name=name,
                                    last_name=last_name, 
                                    email=email, 
                                    address=address, 
                                    zip_code=zip_code, 
                                    city=city, 
                                    mobile=mobile, 
                                    total=total)

    for item in Cart(request):
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            vendor=item['product'].vendor,
            price = item['product'].price,
            quantity=item['quantity']
        )
        order.vendors.add(item['product'].vendor)

    return order


def notificar_vendedor(orden):
    from_email = settings.EMAIL_HOST_USER

    for vendors in orden.vendors.all():
        to_email = user.paypal_email
        subject = 'New orden'
        text_content = 'Tienes una nueva orden'
        html_content = render_to_string('orderes/noti_vendedor.html', {'orden':orden, 'vendors':vendors})

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()


def notificar_cliente(orden):
    from_email = settings.EMAIL_HOST_USER

    to_email = order.email
    subject = 'Confirmacion de orden'
    text_content = 'Gracias por su orden'
    html_content = render_to_string('orderes/noti_cliente.html', {'order':order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

