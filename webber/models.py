from django.db import models
from django.contrib import  admin

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Content(models.Model):
    content = models.TextField(blank=True)
    who = models.CharField(blank=True, max_length=128)

    def __str__(self):
        return self.content
