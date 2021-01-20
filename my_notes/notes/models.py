from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tag(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name="notes", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title + " : " + self.content
