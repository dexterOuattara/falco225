from django.contrib import admin
from .models import FollowersCount, LikePost, Profile, Post, Course

# Register your models here.

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
