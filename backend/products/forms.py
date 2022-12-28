from django.forms import ModelForm
from django import forms
from django.forms import ImageField, FileInput

from . models import Product

class AddToCart(forms.Form):
    quantity = forms.IntegerField()

class ProductForm(ModelForm):
    image = ImageField(widget=FileInput)
    class Meta:
        model = Product
        fields = ['category', 'image', 'name', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['category'].widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        self.fields['image'].widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        self.fields['name'].widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900  sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        self.fields['description'].widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900  sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
        self.fields['price'].widget.attrs['class'] = 'bg-gray-50 border border-gray-300 text-gray-900  sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'


        self.fields['category'].widget.attrs['placeholder'] = 'category'
        self.fields['image'].widget.attrs['placeholder'] = 'image'
        self.fields['name'].widget.attrs['placeholder'] = 'name'
        self.fields['description'].widget.attrs['placeholder'] = 'description'
        self.fields['price'].widget.attrs['placeholder'] = 'Price'
