from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.content
