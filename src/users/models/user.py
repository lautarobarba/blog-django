from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.urls import reverse

class UserManager(BaseUserManager):

    def create_user(self, email=None, password=None, is_admin=False):
        if not email:
            raise ValueError('El usuario necesita un email')
        
        if not password:
            raise ValueError('El usuario necesita contraseña')
        
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.admin = is_admin
        user_obj.is_superuser = is_admin
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email=None, password=None):
        user_obj = self.create_user(email=email, password=password, is_admin=True)
        return user_obj

# To use this class globaly don't forget to set AUTH_USER_MODEL = 'users.User' in main settings.py file
class User(PermissionsMixin, AbstractBaseUser):
    
    email = models.EmailField(max_length=255, unique=True)
    admin = models.BooleanField(default=False)

    # New manager
    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [] #USERNAME_FIELD and password are required by default

    def get_username(self):
        return self.email

    def __str__(self):
        return self.email

    def is_admin(self):
        return self.admin
    
    # Required by admin app
    def is_staff(self):
        return self.admin

    # Redirect url after creation
    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk':self.profile.pk})