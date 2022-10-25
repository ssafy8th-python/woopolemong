# import os
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField
from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Portfolio(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    p_link = models.CharField(max_length=100, null=True)
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
    # def delete(self, *args, **kargs):
    #     if self.image:
    #         os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
    #     super(Portfolio_image, self).delete(*args, **kargs)
