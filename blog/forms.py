from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import BlogPost


class RegistrationForm(UserCreationForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'image', 'password1', 'password2']


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "content"]
        # fields = '__all__'



class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
    