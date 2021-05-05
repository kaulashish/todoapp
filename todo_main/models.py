from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.conf import settings

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    heading = models.CharField(max_length=225)
    note = models.TextField(max_length=500, blank=True, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ["completed"]
