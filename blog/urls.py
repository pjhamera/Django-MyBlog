'''Defines URL patterns for blog.'''
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path("", views.StartingPageView.as_view(), name="index"),
    # Displays all blogposts 
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    # Display a single blogpost
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
    ]