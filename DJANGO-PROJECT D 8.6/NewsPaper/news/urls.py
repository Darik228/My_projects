from django.urls import path
from .views import PostSearch, PostList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, BaseRegisterView, upgrade_me
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', PostList.as_view()),
    path('search/', PostSearch.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('create/login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('create/logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
    path('create/upgrade/', upgrade_me, name='upgrade')
]