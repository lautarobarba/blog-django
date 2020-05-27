from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post

class PostCreateView(LoginRequiredMixin, CreateView):
    
    login_url = '/user/login/'
    template_name = 'posts/post_new.html'
    model = Post
    fields = ['title', 'content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)