from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages

def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog/home.html', {'posts': posts, 'categories': categories})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Please log in to comment.')
            return redirect('accounts:login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('blog:detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, 'Post created successfully!')
            return redirect('blog:detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all()
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})