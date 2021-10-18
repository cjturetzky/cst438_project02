from django.db import models
# extend the existing user model
from django.contrib.auth.models import User

from PIL import Image

# Create your models here.
class Profile(models.Model):
    # 1 to 1 relationship with user model
    #(CASCADE)if user is deleted them profile is deleted, but if profile is deleted wont delete user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    #use save class of our parent class(Pillow)
    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

