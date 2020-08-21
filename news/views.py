from django.shortcuts import render
from django.views.generic import ListView

from .models import Article, Reporter
# Create your views here.
class NewsPageView(ListView):
    model = Article
    template_name = 'news/news_home.html'
    
class ReporterPageView(ListView):
    model = Reporter
    template_name = 'news/reporter_view.html'
        
    

