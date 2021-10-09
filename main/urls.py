from django.contrib import admin
from django.urls import path
from . import views

#import views

urlpatterns = [
    path('', views.home, name='page-home'),
    path('about/', views.about, name='page-about'),
]