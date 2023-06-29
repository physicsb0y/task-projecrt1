from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from .views import blog_post_list

# app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('create_post', views.create_post, name='create_post'),
    path('post/<int:post_id>', views.post_content, name='post_content'),
    path('update/<int:post_id>', views.update_post, name='post_update'),
    path('search', views.blog_post_search, name='blog_post_search'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('api/posts/', blog_post_list, name='api-post-lists'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
