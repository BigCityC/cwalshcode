from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    #author = models.ForeignKey(User)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
