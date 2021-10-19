from django.contrib import admin
from django.urls import path
from . import views

from .views import (WishListView,
                    WishDetailView,
                    WishCreateView
)

#import views

urlpatterns = [
    path('', WishListView.as_view(), name='wishlist-home'),
    path('wish/<int:pk>', WishDetailView.as_view(), name='wishlist-detail'),
    path('wish/new/', WishCreateView.as_view(), name='wishlist-create'),
    path('about/', views.about, name='wishlist-about'),
]