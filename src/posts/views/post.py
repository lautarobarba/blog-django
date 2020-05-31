from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from posts.models import Post
from posts.views.mixins import PostOwnerMixin
from users.views.mixins import GroupContextMixin
from django.urls import reverse_lazy

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_create.html'
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

class PostDetailView(PostOwnerMixin, DetailView):
    model = Post

class PostListView(GroupContextMixin, ListView):
    template_name = 'posts/post_list.html'
    model = Post
    queryset = Post.objects.order_by('-last_modified')
    paginate_by = 5

class PostUserListView(GroupContextMixin, ListView):
    template_name = 'posts/post_list.html'
    model = Post
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.author_id = self.kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Post.objects.filter(author__id=self.author_id)

class PostUpdateView(PostOwnerMixin, LoginRequiredMixin, UpdateView):
    template_name = 'posts/post_update.html'
    model = Post
    fields = ['title', 'content']

class PostDeleteView(PostOwnerMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('home')