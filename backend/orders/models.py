from django.db import models
from products.models import Product
from users.models import User

class Order(models.Model):
    customer        = models.ForeignKey(User, related_name='ordenes', on_delete=models.CASCADE, null=True)
    name            = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
    email           = models.CharField(max_length=100)
    address         = models.CharField(max_length=100)
    zip_code        = models.CharField(max_length=100)
    city            = models.CharField(max_length=100)
    mobile          = models.CharField(max_length=100)
    date            = models.DateTimeField(auto_now_add=True)
    total           = models.DecimalField(max_digits=8, decimal_places=2)
    vendors         = models.ManyToManyField(User, related_name='orders')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.customer.username

class OrderItem(models.Model):
    customer        = models.ForeignKey(User, related_name='itmes', on_delete=models.CASCADE, null=True)
    order           = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product         = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    vendor          = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    is_paid         = models.CharField(max_length=100, null=True, blank=True)
    price           = models.DecimalField(max_digits=8, decimal_places=2)
    quantity        = models.IntegerField(default=1)

    def get_total_price(self):
        return self.price * self.quantity



