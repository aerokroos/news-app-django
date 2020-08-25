from django.contrib import admin
from .models import Reporter, Article, Section, User, Comment
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(Section)
admin.site.register(Comment)





