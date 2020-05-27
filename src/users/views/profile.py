from django.views.generic import DetailView
from users.models import Profile
from django.views.generic.edit import UpdateView

class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProfileUpdateView(UpdateView):
    template_name = 'users/profile_update.html'
    model = Profile
    fields = ['first_name', 'last_name', 'country', 'phone', 'picture']