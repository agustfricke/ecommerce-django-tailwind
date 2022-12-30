from django.contrib import admin
from . models import Category, Product, Review

admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Product)


# Register your models here.
