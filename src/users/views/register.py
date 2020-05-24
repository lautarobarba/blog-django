from django.views.generic.edit import CreateView
from users.forms import UserCreationForm

class UserCreateView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/'