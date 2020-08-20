from django.contrib import admin
from .models import Reporter, Article, Section

# Register your models here.
admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(Section)
