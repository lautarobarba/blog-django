from django.views.generic import DetailView
from users.models import Profile
from django.views.generic.edit import UpdateView

from django.contrib.auth import get_user_model
User = get_user_model()

class ProfileDetailView(DetailView):
    model = Profile

    def get(self, request, *args, **kwargs):
        # User can edit only his own profile
        logged_user_profile = request.user.profile.pk
        current_profile = self.kwargs['pk']
        self.can_edit = logged_user_profile == current_profile
        # User role
        if request.user.profile.admin:
            self.user_role = 'admin'
        else: 
            self.user_role = 'client'
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_edit'] = self.can_edit
        context['user_role'] = self.user_role
        return context

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'users/profile_update.html'
    fields = ['first_name', 'last_name', 'country', 'phone', 'picture']

    def get(self, request, *args, **kwargs):
        # User can edit only his own profile
        logged_user_profile = request.user.profile.pk
        current_profile = self.kwargs['pk']
        self.can_edit = logged_user_profile == current_profile
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_edit'] = self.can_edit
        return context