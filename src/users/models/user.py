from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    pass

# To use this class globaly don't forget to set AUTH_USER_MODEL = 'users.User' in main settings.py file
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
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

    # Methods required by admin app
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
        
    # Methods required by admin app
    def is_staff(self):
        return self.staff
    
    def is_active(self):
        return self.active
