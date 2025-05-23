from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post, Category
from .forms import PostForm
from django.contrib import messages

def home(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    posts = Post.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    if category_slug:
        posts = posts.filter(category__slug=category_slug)

    categories = Category.objects.all()
    return render(request, 'blog/home.html', {'posts': posts, 'categories': categories, 'query': query, 'category_slug': category_slug})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/detail.html', {'post': post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('blog:detail', slug=post.slug)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PostForm()
    return render(request, 'blog/create.html', {'form': form})