from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    query = request.GET.get("q")
    if query:
        post_list = Post.objects.filter(title__icontains=query).order_by("-created_at")
    else:
        post_list = Post.objects.all().order_by("-created_at")
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    return render(request, "blog/home.html", {"posts": posts, "query": query})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("home")


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("home")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("home")
