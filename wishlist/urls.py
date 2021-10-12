from django.contrib import admin
from django.urls import path
from . import views

#import views

urlpatterns = [
    path('', views.home, name='wishlist-home'),
    path('about/', views.about, name='wishlist-about'),
    path('createaccount/', views.createAccount, name='wishlist-createaccount'),
]