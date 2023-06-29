from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import BlogPostSerializer
from .forms import RegistrationForm, BlogPostForm, UpdatePostForm
from .models import BlogPost
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def blog_post_list(request):
    blog_posts = BlogPost.objects.all()
    serializer = BlogPostSerializer(blog_posts, many=True)
    return Response(serializer.data)


@login_required(login_url='login')
def index(request):
    posts = BlogPost.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = BlogPost.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()

    context = {
        'posts': posts
    }

    return render(request, 'blog/index.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/index')
        
        else:
            form = RegistrationForm()
    
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'registration/sign_up.html', context)




@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        
    else:
        form = BlogPostForm()

    return render(request, 'blog/create_post.html', {'form': form})


def blog_post_search(request):
    query = request.GET.get('keyword')

    if query:
        posts = BlogPost.objects.filter(title__icontains=query)
    else:
        posts = []

    context = {
        'posts': posts,
        'query': query,
    }

    return render(request, 'blog/search.html', context)



def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    

def post_content(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/postcontent.html', context)


def update_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        form = UpdatePostForm(request.POST, instance=post)


        if form.is_valid():
            form.save()
            return redirect('post_content', post_id=post.id)
    
    else:
        form = UpdatePostForm(instance=post)

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'blog/update_post.html', context)