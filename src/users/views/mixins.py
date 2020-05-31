from django.views import View
from django.views.generic.base import ContextMixin

class GroupContextMixin(ContextMixin, View):
    """
    Define user's group in context as user_group 
    """
    def get(self, request, *args, **kwargs):
        # Check if user is anonymous
        # anonymous.id is always None
        if request.user.id:
            # User group
            self.user_group = request.user.profile.group.name
        else:
            self.user_group = 'anonymous'
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_group'] = self.user_group
        return context

class ProfileOwnerMixin(GroupContextMixin):
    """
    Allow owners to edit only their profiles
    """
    def get(self, request, *args, **kwargs):
        # Check if user is anonymous
        # anonymous.id is always None
        if request.user.id:
            # User can edit only his own profile
            logged_user_profile = request.user.profile.pk
            current_profile = self.kwargs['pk']
            self.can_edit = logged_user_profile == current_profile
        else:
            self.can_edit = False
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_edit'] = self.can_edit
        return context