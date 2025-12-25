from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    posts = BlogPost.objects.all().order_by('-created_date')
    return render(request, 'blog/index.html', {'posts': posts})

def create_post(request):
    form = BlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'blog/form.html', {'form': form})

def view_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/detail.html', {'post': post})

def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    form = BlogPostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'blog/form.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.delete()
    return redirect('index')
