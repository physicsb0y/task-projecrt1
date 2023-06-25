from django.contrib import admin
from django.contrib.auth.models import Group, Permission

from .models import BlogPost

# Register your models here.


admin.site.register(BlogPost)


default_group = Group.objects.get(name='default')
delete_permission = Permission.objects.get(codename='delete_blogpost')
default_group.permissions.add(delete_permission)
