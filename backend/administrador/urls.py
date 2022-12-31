from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('check/<int:order_id>/', views.check, name='check'),
    path('not_check/<int:order_id>/', views.not_check, name='not_check'),


    path('users/', views.users, name='users'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),

    path('products/', views.products, name='products'),
    path('update_product/<int:pk>/',views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),

    path('categorys/', views.categorys, name='categorys'),
    path('create_category/', views.create_category, name='create_category'),
    path('update_category/<int:pk>/',views.update_category, name='update_category'),
    path('delete_category/<int:pk>/',views.delete_category, name='delete_category'),
] 
