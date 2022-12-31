from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Poner is activae false y limpiar sin custom account manager

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                           **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, username, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(_('bio'), max_length=500, blank=True)
    avatar = models.ImageField(null=True, blank=True, default='/avatar.jpg')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_vendor = models.BooleanField(default=False)
    paypal_email = models.CharField(max_length=150, unique=True, blank=True, null=True)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def balance(self):
        items = self.items.filter(is_paid=False, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)
    
    def pagado(self):
        items = self.items.filter(is_paid=True, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)




