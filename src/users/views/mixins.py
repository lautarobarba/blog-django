from django.views import View
from django.views.generic.base import ContextMixin

class GroupContextMixin(ContextMixin, View):
    """
    Define user's gruop in context as user_group 
    """

    def get(self, request, *args, **kwargs):
        # User group
        if request.user
            if request.user.profile.admin:
                self.user_role = 'admin'
            else: 
                self.user_role = 'client'
            return super().get(request, *args, **kwargs)