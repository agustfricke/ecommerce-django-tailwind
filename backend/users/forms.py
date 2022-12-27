from django.contrib.auth.forms import UserCreationForm
from . models import User
from django.forms import ModelForm
from django.forms import ImageField, FileInput


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'
        self.fields['username'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'
        self.fields['password1'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'
        self.fields['password2'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'


        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'


