from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey('accounts.User', related_name='portfolios', on_delete=models.SET_NULL, NULL=True)
    category = models.CharField(max_lenth=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
