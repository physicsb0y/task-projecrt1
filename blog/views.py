from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, BlogPostForm
from .models import BlogPost
# Create your views here.

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

