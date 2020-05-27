from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# User set in global settings
User = get_user_model()

class Profile(models.Model):

    COUNTRIES = [
        ('AR', 'Argentina'),
        ('CH', 'Chile'),
        ('BR', 'Brasil'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=2, null=True, choices=COUNTRIES, default='AR')
    phone = models.CharField(max_length=12, null=True, blank=True)
    picture = models.ImageField()

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'{self.user.email}'

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk':self.pk})
