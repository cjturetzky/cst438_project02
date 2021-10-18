from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class WishlistItem(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    wname = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    img = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.wname

class Wish(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title