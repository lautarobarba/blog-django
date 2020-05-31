from users.views.mixins import GroupContextMixin
from posts.models import Post

class PostOwnerMixin(GroupContextMixin):
    """
    Allow authors to edit only their own posts
    """
    def get(self, request, *args, **kwargs):
        # Check if user is anonymous
        # anonymous.id is always None
        if request.user.id:
            # Authors can edit only their own posts
            logged_user_id = request.user.id
            post = Post.objects.get(id=self.kwargs['pk'])
            author_id = post.author.id
            self.can_edit = logged_user_id == author_id
        else:
            self.can_edit = False
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_edit'] = self.can_edit
        return context