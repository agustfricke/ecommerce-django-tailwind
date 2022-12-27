from django.urls import path
from . import views

urlpatterns = [
    path('my_profile/', views.my_profile, name='my_profile')
] 
