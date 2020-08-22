from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Article, Reporter, User
from django.urls import reverse_lazy

from .forms import RegisterForm

# Create your views here.
class NewsPageView(ListView):
    model = Article
    template_name = 'news/news_home.html'
    
class ReporterPageView(ListView):
    model = Reporter
    template_name = 'news/reporter_view.html'

class SignupCreatePage(CreateView):
    form_class = RegisterForm
    template_name = 'news/signup.html'
    succes_ulr = reverse_lazy('home')
        

