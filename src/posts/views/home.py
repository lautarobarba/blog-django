from django.views.generic import ListView
from posts.models import Post

class HomeView(ListView):

    template_name = 'posts/home.html'
    model = Post
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
