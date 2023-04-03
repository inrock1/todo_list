from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(required=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return self.content
