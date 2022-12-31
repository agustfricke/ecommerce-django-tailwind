from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm
from . models import User
from django import forms
from django.forms import ModelForm
from django.forms import ImageField, FileInput

class PasswordResetForm(PasswordResetForm):

    fields = ['email']
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'

        self.fields['email'].widget.attrs['placeholder'] = ' Email'



class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'
        self.fields['new_password2'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'

        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        



class BecomeVendorForm(ModelForm):
    class Meta:
        model = User
        fields = ['paypal_email']

    def __init__(self, *args, **kwargs):
        super(BecomeVendorForm, self).__init__(*args, **kwargs)

        self.fields['paypal_email'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'


        self.fields['paypal_email'].widget.attrs['placeholder'] = 'PayPal Email'


class UpdateProfileForm(ModelForm):
    avatar = ImageField(widget=FileInput)
    class Meta:
        model = User
        fields = ['email', 'username', 'bio', 'avatar']

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'
        self.fields['username'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'
        self.fields['bio'].widget.attrs['class'] = ' text-negro sm:text-sm rounded-lg  block w-full p-2.5  dark:placeholder-gray-400'
        self.fields['avatar'].widget.attrs['class'] = ' block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'


        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['bio'].widget.attrs['placeholder'] = 'Biografy'
        self.fields['avatar'].widget.attrs['placeholder'] = 'Profile Image'


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


