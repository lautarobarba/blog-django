from django.views.generic.edit import CreateView
from  import VisitorForm

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = VisitorForm
    success_url = '/thanks/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context