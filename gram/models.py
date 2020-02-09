from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    image_caption = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(value = 0)
    comments = models.TextField(max_length= 30 )
    image_name = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    def save_image(self):
        self.save()

class Profile(models.Model):
    profile_image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    bio = models.TextField(max_length=100)
    