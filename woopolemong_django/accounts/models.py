from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.processors import Thumbnail
from imagekit.models import ImageSpecField

# Create your models here.
class User(AbstractUser):

    def user_image_path(instance, filename):
        return f'images/{instance.user.username}/{filename}'

    intro = models.TextField(default="")
    my_image = models.ImageField(blank=True, upload_to=user_image_path)
    my_image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(100, 100)],
        format='JPEG',
        options={'quality': 80},
    )