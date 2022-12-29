from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('update_order/<int:pk>/', views.update_order, name='update_order'),

    path('users/', views.users, name='users'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),

    path('products/', views.products, name='products'),
    path('update_product/<int:pk>/',views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
] 
