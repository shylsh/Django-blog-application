from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all().order_by("-created_at")  # Fetch all posts
    return render(
        request, "blog/home.html", {"posts": posts}
    )  # Pass the posts to the template
