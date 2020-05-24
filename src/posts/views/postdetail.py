from django.views.generic import DetailView
from posts.models import Post

class PostDetailView(DetailView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context