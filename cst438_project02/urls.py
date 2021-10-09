"""cst438_project02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

#import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    # path('',views.home),
    # path('products/', views.products),
    # path('customer/', views.customer),
    # path('create/',views.create, name='create'),
    # path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# this url takes you to the page that explains these things more and why they may be needed: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website
# This is commented out for now but may be needed in the future
# Definition: This new item includes a path() that forwards requests with the pattern catalog/
# to the module catalog.urls (the file with the relative URL catalog/urls.py) als0 will need
# the import from above.
# urlpatterns += [
#     path('catalog/', include('catalog.urls')),
# ]

# from django.conf import settings
# from django.conf.urls.static import static
#
#
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
