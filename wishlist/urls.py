from django.contrib import admin
from django.urls import path
from . import views

from .views import (WishListView,
                    WishDetailView,
                    WishCreateView,
                    WishUpdateView,
                    WishDeleteView,
                    UserWishListView

)

#import views

urlpatterns = [
    path('', WishListView.as_view(), name='wishlist-home'),
    path('user/<str:username>/', UserWishListView.as_view(), name='user-wishlist'),
    path('wish/<int:pk>/', WishDetailView.as_view(), name='wishlist-detail'),
    path('wish/new/', WishCreateView.as_view(), name='wishlist-create'),
    path('wish/<int:pk>/update/', WishUpdateView.as_view(), name='wishlist-update'),
    path('wish/<int:pk>/delete/', WishDeleteView.as_view(), name='wishlist-delete'),
    path('about/', views.about, name='wishlist-about'),
]