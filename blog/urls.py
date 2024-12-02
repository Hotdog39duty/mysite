# blog/urls.py
"""
URL configuration for the blog app.
This module defines the URL patterns for the blog application, mapping URLs to their corresponding view functions.
URL Patterns:
- '' : Displays the list of blog posts.
- '<int:post_id>/' : Displays the details of a specific blog post.
- 'signup/' : Displays the signup form.
- 'login/' : Displays the login form.
- 'add_post/' : Displays the form to add a new blog post.
- 'post/<int:post_id>/add_review/' : Displays the form to add a review to a specific blog post.
- 'dashboard/' : Displays the user dashboard.
"""
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('add_post/', views.add_post, name='add_post'),
    path('post/<int:pk>/add_review/', views.add_review, name='add_review'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.index, name='index'),  # Home page for the blog
]
