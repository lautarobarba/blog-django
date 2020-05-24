from django.urls import path
from .views import HomeView, PostCreateView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new', PostCreateView.as_view(), name='post-new'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
]
