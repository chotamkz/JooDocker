from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    creater_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
