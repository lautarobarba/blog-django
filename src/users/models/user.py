from django.db import models
from django.contrib.auth.models import User

class Visitor(models.Model):
    ROLE = [
        ('A', 'Admin'),
        ('U', 'User'),
    ]
    role = models.CharField(max_length=1, choices=ROLE, default='U')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField('profile picture', null=True, blank=True)

    def __str__(self):
        return F'Username: {self.username}. Name:{self.first_name}, {self.last_name}. Role:{self.role}'
