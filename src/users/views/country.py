from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Country
from django.urls import reverse_lazy

class CountryCreateView(LoginRequiredMixin, CreateView):
    model = Country
    template_name = 'users/country_create.html'
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        if request.user.profile.admin:
            self.user_role = 'admin'
        else:
            self.user_role = 'client'
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_role'] = self.user_role
        return context

class CountryListView(LoginRequiredMixin, ListView):
    model = Country
    queryset = Country.objects.order_by('name')

    def get(self, request, *args, **kwargs):
        if request.user.profile.admin:
            self.user_role = 'admin'
        else:
            self.user_role = 'client'
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_role'] = self.user_role
        return context

class CountryUpdateView(LoginRequiredMixin, UpdateView):
    model = Country
    template_name = 'users/country_update.html'
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        if request.user.profile.admin:
            self.user_role = 'admin'
        else:
            self.user_role = 'client'
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_role'] = self.user_role
        return context

class CountryDeleteView(LoginRequiredMixin, DeleteView):
    model = Country
    template_name = 'users/country_delete.html'
    success_url = reverse_lazy('country-list')

    def get(self, request, *args, **kwargs):
        if request.user.profile.admin:
            self.user_role = 'admin'
        else:
            self.user_role = 'client'
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_role'] = self.user_role
        return context