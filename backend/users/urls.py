from django.urls import path
from . import views

urlpatterns = [
    path('update_profile/', views.update_profile, name='update_profile'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('register_page/', views.register_page, name='register_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout_user/', views.logout_user, name='logout_user'),
    # 
] 
