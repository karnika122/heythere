from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    # making profile relation with users table -
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    
   
    # Added this dunder method to show profile of users
    # as string into admin panel
    def __str__(self):
         return f'{self.user.username} Profile'

    def save(self):
        super().save() # calling parent class save method

        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)     