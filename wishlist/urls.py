#rest framework
from rest_framework.urlpatterns import format_suffix_patterns
#
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

from wishlist import views as wish_views

#login views
from django.contrib.auth import views as auth_views

#import media
from django.conf import settings
from django.conf.urls.static import static
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
    path('wishes/', views.wishapi.as_view()),
    path('wishes/<int:id>/', views.wishapi.as_view())
    
    # path('createaccount/', views.createAccount, name='wishlist-createaccount'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)