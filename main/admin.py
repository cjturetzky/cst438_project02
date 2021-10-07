from django.contrib import admin
from .models import Users, WishlistItem

# Register your models here.
admin.site.register(Users);
admin.site.register(WishlistItem);