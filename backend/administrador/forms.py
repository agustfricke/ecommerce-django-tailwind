from orders.models import OrderItem
from products.models import Category
from django.forms import ModelForm
from django import forms
from tinymce.widgets import TinyMCE


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)

        self.fields['subject'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'
        self.fields['receivers'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'
        self.fields['message'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'


        self.fields['subject'].widget.attrs['placeholder'] = 'Subjet'
        self.fields['receivers'].widget.attrs['placeholder'] = 'Recibers'
        self.fields['message'].widget.attrs['placeholder'] = 'Message'



class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'


        self.fields['name'].widget.attrs['placeholder'] = 'Name'

