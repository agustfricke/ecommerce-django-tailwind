from django.db import models
from users.models import User



class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    category        = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor          = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    name            = models.CharField(max_length=255)
    slug            = models.SlugField(max_length=255)
    description     = models.TextField(max_length=255)
    date            = models.DateTimeField(auto_now_add=True)
    price           = models.DecimalField(max_digits=6, decimal_places=2)
    image           = models.ImageField(default='/product.jpg', blank=True, null=True)
    num_reviews     = models.IntegerField(null=True, blank=True, default=0)
    rating          = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    count_in_stock  = models.IntegerField(null=True, blank=True, default=0)



    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name 


class Review(models.Model):
    product         = models.ForeignKey(Product,related_name='review', on_delete=models.SET_NULL, null=True)
    user            = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating          = models.IntegerField(null=True, blank=True, default=0)
    comment         = models.TextField(null=True, blank=True)
    date            = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.rating)