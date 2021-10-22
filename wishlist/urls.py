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

#import views

urlpatterns = [
    path('', views.home, name='wishlist-home'),
    path('about/', views.about, name='wishlist-about'),
    path('wishs/', views.wishapi.as_view())
    
    # path('createaccount/', views.createAccount, name='wishlist-createaccount'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)