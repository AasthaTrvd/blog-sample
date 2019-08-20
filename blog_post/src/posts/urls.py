from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from . import views
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import url

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path("/", PostListView.as_view(), name="blog-home"),
