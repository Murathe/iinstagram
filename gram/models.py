from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class IMage(models.Model):
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    image_caption = models.CharField(max_length=50)
    