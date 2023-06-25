from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('create_post', views.create_post, name='create_post'),
]
