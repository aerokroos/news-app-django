from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Article, Reporter, User, Comment
from django.urls import reverse_lazy

from .forms import RegisterForm, ReporterForm, ArticleForm

# Create your views here.
class NewsPageView(ListView):
    model = Article
    template_name = 'news/news_home.html'
    context_object_name = 'articles'
    
    def get_context_data(self, **kwargs):
        comment = super(NewsPageView, self).get_context_data(**kwargs)
        comment['comments'] = Comment.objects.all()
        return comment

    
class SearchView(ListView):
    model = Article
    template_name = 'news/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            title = Article.objects.filter(title__contains=query)
            result = title
        else:
            result = None
        
        return result
        




class CreateCommentPageView(CreateView):
    model = Comment
    template_name = 'news/news_home.html'

class ReporterPageView(ListView):
    model = Reporter
    template_name = 'news/reporter_view.html'

class SignupCreatePage(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'news/signup.html'

class CreateReporterPageView(CreateView):
    model = Reporter
    form_class = ReporterForm
    template_name = 'news/new_reporter.html'
    success_url = reverse_lazy('news_home')

class CreateArticlePageView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'news/new_article.html'
    success_url = reverse_lazy('news_home')

    def form_valid(self, form):
        form.instance.article_reporter = self.request.user
        return super().form_valid(form)

class PoliticsPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/politics.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Politics')

class EducationPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/education.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Education')

class SportsPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/sports.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Sports')

class SciencePageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/science.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Science')

class EntertainmentPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/entertainment.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Entertainment')

class TechnologyPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/technology.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Technology')

class EconomyPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/economy.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Economy')

class ArtsPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/arts.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Arts')

class WeatherPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/weather.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Weather')

class FashionPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/fashion.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Fashion')

class HealthPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/health.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Health')













        



    

    

    
    
    
   

