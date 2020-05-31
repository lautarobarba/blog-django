from django.db import models
from django.urls import reverse

# Custom User
from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    title = models.CharField(verbose_name='título', max_length=255)
    created = models.DateTimeField(verbose_name='creado', auto_now_add=True)
    last_modified = models.DateTimeField(verbose_name='modificado', auto_now=True)
    author = models.ForeignKey(User, verbose_name='autor', null=True, on_delete=models.SET_NULL)
    content = models.TextField(verbose_name='contenido', null=True, blank=True)

    def __str__(self):
        if self.author:
            return f'{self.title} de {self.author.profile}'
        else:
            return f'{self.title} de {self.author}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.id})