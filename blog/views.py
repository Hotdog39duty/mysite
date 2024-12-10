# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Post, Review
from .forms import PostForm, ReviewForm
from .models import Review


def home(request):
    """
    Render the home page.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered home page.
    :rtype: HttpResponse
    """
    return render(request, 'home.html')


@login_required
def add_post(request):
    """
    Handle the submission of a new blog post.

    This view requires the user to be logged in. It handles both the display
    of the post form and the processing of the form submission.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: If the request method is POST and the form is valid, it redirects
             to the post list page. Otherwise, it renders the post form page.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})


@login_required
def add_review(request, pk):
    """
    Handle the submission of a review for a specific blog post.

    This view requires the user to be logged in. It handles both the display
    of the review form and the processing of the form submission.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param pk: The ID of the blog post to which the review is being added.
    :type pk: int
    :return: If the request method is POST and the form is valid, it redirects
             to the post detail page. Otherwise, it renders the review form page.
    :rtype: HttpResponse
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.post = post
            review.user = request.user
            review.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = ReviewForm()
    return render(request, 'blog/add_review.html', {'form': form, 'post': post})


def blog_list(request):
    """
    Display a list of all blog posts.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered blog post list page.
    :rtype: HttpResponse
    """
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    """
    Display the details of a specific blog post.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param pk: The ID of the blog post to display.
    :type pk: int
    :return: The rendered blog post detail page.
    :rtype: HttpResponse
    """
    post = get_object_or_404(Post, pk=pk)
    reviews = post.reviews.all()  # Assuming a reverse relation
    return render(request, 'post_detail.html', {'post': post, 'reviews': reviews})


def login_view(request):
    """
    Handle user login.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: If the request method is POST and the form is valid, it redirects
             to the blog list page. Otherwise, it renders the login form page.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:blog_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    """
    Handle user signup.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: If the request method is POST and the form is valid, it redirects
             to the login page. Otherwise, it renders the signup form page.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def user_dashboard(request):
    """
    Display the user's dashboard with their posts and reviews.

    This view requires the user to be logged in.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered user dashboard page.
    :rtype: HttpResponse
    """
    user_reviews = Review.objects.filter(user=request.user)
    return render(request, 'blog/user_dashboard.html', {
        'user_posts': Post.objects.filter(author=request.user),
        'user_reviews': user_reviews
    })


def index(request):
    """
    Display the index page with a list of all blog posts.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered index page.
    :rtype: HttpResponse
    """
    posts = Post.objects.all().order_by('-created_at')  # Get all posts
    return render(request, 'blog/index.html', {'posts': posts})
