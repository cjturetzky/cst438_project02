
from django.contrib import admin
from .models import Users, WishlistItem, Wish

# Register your models here.
admin.site.register(Users);
admin.site.register(WishlistItem);
admin.site.register(Wish);