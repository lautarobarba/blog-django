from django import forms
from django.contrib.auth import get_user_model
#from users.models import Profile

User = get_user_model()

class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

class UserUpdateForm(forms.ModelForm):
    pass
    #Hacer cambio de contraseña
    #Hacer cambio de email
