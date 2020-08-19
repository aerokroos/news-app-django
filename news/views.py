from django.shortcuts import render
from django.views.generic import ListView

from .models import New, Reporter
# Create your views here.
class NewsPageView(ListView):
    model = New
    template_name = 'news/news_home.html'
    
        
    

