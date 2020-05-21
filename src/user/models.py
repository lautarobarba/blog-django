from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True)
