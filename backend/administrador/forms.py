from orders.models import OrderItem
from products.models import Category
from django.forms import ModelForm


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

