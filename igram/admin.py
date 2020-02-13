from django.contrib import admin
from .models import Image, Comments, Followers, PhotoLikes, Profile

# Register your models here.

admin.site.register(Image)
admin.site.register(Comments)
admin.site.register(Followers)
admin.site.register(PhotoLikes)
admin.site.register(Profile)