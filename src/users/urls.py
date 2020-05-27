from django.urls import path
from .views import UserCreateView, UserLoginView, UserLogoutView, ProfileDetailView

urlpatterns = [
    path('new/', UserCreateView.as_view(), name='user-new'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    # USER DELETE path('')
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    #path('profile/update/<:>/', UserLogoutView.as_view(), name='profile-update'),
    #path('profile/delete/<:>/', UserLogoutView.as_view(), name='profile-delete'),
]