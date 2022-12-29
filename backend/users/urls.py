from django.urls import path
from . import views

urlpatterns = [
    path('vendor_products/', views.vendor_products, name='vendor_products'),
    path('create_vendor/', views.create_vendor, name='create_vendor'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('register_page/', views.register_page, name='register_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    path('vendor_earnings/', views.vendor_earnings, name='vendor_earnings'),
] 
