from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    last_request_time = models.DateTimeField(blank=True, null=True)
    last_request_text = models.TextField(blank=True)
