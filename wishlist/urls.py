from django.contrib import admin
from django.urls import path
from . import views

#import views

urlpatterns = [
    path('', views.home, name='wishlist-home'),
    path('about/', views.about, name='wishlist-about'),
    path('api/getItems', views.getItems, name='api-getitems')
    # path('createaccount/', views.createAccount, name='wishlist-createaccount'),
    
]