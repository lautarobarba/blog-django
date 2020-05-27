from django.views.generic.edit import CreateView, DeleteView
from users.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from users.models import Profile
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateView(CreateView):
    template_name = 'users/user_create.html'
    form_class = UserCreationForm

    def post(self, request, *args, **kwargs):

        #boolean contraseñas iguales y validadores
        #Guardar mensajes de error

        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            new_profile = Profile(user=new_user)
            new_profile.save()
            login(request, new_user)
            return redirect(new_user)
        else:
            #Agregar mensaje de error
            return redirect('user-new')

class UserLoginView(LoginView):
    template_name = 'users/user_login.html'

class UserLogoutView(LogoutView):
    template_name = 'users/user_logout.html'

class UserDeleteView(DeleteView):
    template_name = 'users/user_delete.html'
    model = User
    success_url = reverse_lazy('home')