from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class WishlistItem(models.Model):
    wname = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    img = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.wname