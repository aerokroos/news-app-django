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

class CreateCommentPageView(CreateView):
    model = Comment
    template_name = 'news/news_home.html'

class ReporterPageView(ListView):
    model = Reporter
    template_name = 'news/reporter_view.html'

class SignupCreatePage(CreateView):
    form_class = RegisterForm
    template_name = 'news/signup.html'
    succes_url = reverse_lazy('login')

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



        



    

    

    
    
    
   

