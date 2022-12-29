from orders.models import Order, OrderItem
from django.forms import ModelForm

class UpdateOrderItem(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['is_paid']