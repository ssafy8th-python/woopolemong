from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField
from django.db import models
from django.conf import settings


# Create your models here.
class Portfolio(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Portfolio_image(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200, 300)],
        format='JPEG',
        options={'quality': 80},
    )