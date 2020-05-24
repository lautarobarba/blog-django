from django.contrib.auth.views import LogoutView

class UserLogoutView(LogoutView):
    template_name = 'logout.html'