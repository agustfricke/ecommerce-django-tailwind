from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    category    = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor      = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    name        = models.CharField(max_length=255)
    slug        = models.SlugField(max_length=255)
    description = models.TextField(max_length=255)
    date        = models.DateTimeField(auto_now_add=True)
    price       =  models.DecimalField(max_digits=6, decimal_places=2)
    image       = models.ImageField(default='/product.jpg', blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name 