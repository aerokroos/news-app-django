from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import New
# Create your views here.
class NewsPageView(ListView):
    model = New
    template_name = 'news/news_home.html'

