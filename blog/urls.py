from django.urls import path
from .views import home, signup, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
# In the code snippet above, we have defined the URL patterns for the blog app. The URL patterns are mapped to the views that will be rendered when the user visits the corresponding URL. The URL patterns are defined using the path() function from Django's URL dispatcher. The path() function takes three arguments: the URL pattern, the view function, and an optional name for the URL pattern. The URL patterns are defined as follows:
