from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from users.models import Profile

#class ProfileCreateView(CreateView):
    #template_name = 'profile_creation.html'
    #success_url = '/'

class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context