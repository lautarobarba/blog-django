from django.urls import path
from posts.views import (
    PostCreateView, PostDetailView, PostListView, PostUserListView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/new/', PostCreateView.as_view(), name='post-new'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/user/<int:pk>', PostUserListView.as_view(), name='post-user-list'),
]
