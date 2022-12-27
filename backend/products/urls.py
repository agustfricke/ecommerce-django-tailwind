from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('category/<str:slug>/', views.category, name='category'),
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('create/', views.create, name='create'),
] 
