from django.shortcuts import render, redirect
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import auth  # authentication
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from posts.forms import LoginForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import PostModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


# Function to login
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "User logged in successfully")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")
    else:
        form = LoginForm()
        return render(request, "accounts/login.html", {"form": form})


def logout(request):
    django_logout(request)
    return render(request, "logout.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Account created successfully!")
            return redirect("login")
    else:
        form = UserCreationForm()
        return render(request, "register.html", {"form": form})


# Create your views here.
class PostListView(ListView):
    model = PostModel
    template_name = "home.html"
    context_object_name = "posts"
    ordering = ["-published"]

    # Pagination, (?page=2)
    paginate_by = 2


class PostDetailView(DetailView):
    model = PostModel
    template_name = "post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = PostModel
    template_name = "postmodel_form.html"
    fields = ["title", "content"]

    # method to assign username to author for updating author name
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# UpdateView
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostModel
    template_name = "postmodel_form.html"
    fields = ["title", "content"]

    # method to assign username to author for updating author name in post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # function to permit editing post based on their ownership
    def test_func(self):
        # get current working post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostModel
    template_name = "post_confirm_delete.html"
    success_url = "/"

    def test_func(self):
        # get current working post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def profile(request):
    return render(request, "profile.html")


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {"user_form": user_form, "profile_form": profile_form}

    return render(request, "profile.html", context)

