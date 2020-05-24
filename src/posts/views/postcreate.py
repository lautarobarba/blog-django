from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post

class PostCreateView(LoginRequiredMixin, CreateView):
    
    login_url = '/login/'
    template_name = 'posts/create.html'
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)