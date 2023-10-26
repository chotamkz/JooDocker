from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    creator_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
