from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from .models import Article, Reporter, User, Comment
from django.urls import reverse_lazy
from django.db.models import Q

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

    def dispatch(self, *args, **kwargs):
        try:
            return super(NewsPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)
    
class SearchView(ListView):
    model = Article
    template_name = 'news/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            # Search 
            search = Article.objects.filter(
                title__contains=query) | Article.objects.filter(
                sub_title__contains = query) | Article.objects.filter(
                    section__name_section__contains = query)

            result = search
        else:
            result = None
        
        return result
    
    def dispatch(self, *args, **kwargs):
        try:
            return super(SearchView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class ArticlePageView(DetailView):
    model = Article
    template_name = 'news/article.html'
    context_object_name = 'article'

    def dispatch(self, *args, **kwargs):
        try:
            return super(ArticlePageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class CreateCommentPageView(CreateView):
    model = Comment
    template_name = 'news/news_home.html'

    def dispatch(self, *args, **kwargs):
        try:
            return super(CreateCommentPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class ReporterPageView(DetailView):
    model = Reporter
    template_name = 'news/reporter_view.html'
    context_object_name = 'reporter'

    def dispatch(self, *args, **kwargs):
        try:
            return super(ReporterPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class SignupCreatePage(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'news/signup.html'

    def dispatch(self, *args, **kwargs):
        try:
            return super(SignupCreatePage, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class CreateReporterPageView(CreateView):
    model = Reporter
    form_class = ReporterForm
    template_name = 'news/new_reporter.html'
    success_url = reverse_lazy('news_home')

    def dispatch(self, *args, **kwargs):
        try:
            return super(CreateReporterPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class CreateArticlePageView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'news/new_article.html'
    success_url = reverse_lazy('news_home')

    def form_valid(self, form):
        form.instance.article_reporter = self.request.user
        return super().form_valid(form)

    def dispatch(self, *args, **kwargs):
        try:
            return super(CreateArticlePageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class PoliticsPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/politics.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Politics')
    
    def dispatch(self, *args, **kwargs):
        try:
            return super(PoliticsPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class EducationPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/education.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Education')

    def dispatch(self, *args, **kwargs):
        try:
            return super(EducationPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class SportsPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/sports.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Sports')

    def dispatch(self, *args, **kwargs):
        try:
            return super(SportsPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class SciencePageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/science.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Science')

    def dispatch(self, *args, **kwargs):
        try:
            return super(SciencePageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class EntertainmentPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/entertainment.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Entertainment')

    def dispatch(self, *args, **kwargs):
        try:
            return super(EntertainmentPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class TechnologyPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/technology.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Technology')

    def dispatch(self, *args, **kwargs):
        try:
            return super(TechnologyPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class EconomyPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/economy.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Economy')
    
    def dispatch(self, *args, **kwargs):
        try:
            return super(EconomyPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class ArtsPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/arts.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Arts')

    def dispatch(self, *args, **kwargs):
        try:
            return super(ArtsPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class WeatherPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/weather.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Weather')
    
    def dispatch(self, *args, **kwargs):
        try:
            return super(WeatherPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class FashionPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/fashion.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Fashion')
    
    def dispatch(self, *args, **kwargs):
        try:
            return super(FashionPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)

class HealthPageView(ListView):
    context_object_name = 'articles'
    template_name = 'news/health.html'
    
    def get_queryset(self):
        return Article.objects.filter(section__name_section__contains='Health')

    def dispatch(self, *args, **kwargs):
        try:
            return super(HealthPageView, self).dispatch(*args, **kwargs)
        except ImmediateHttpResponse as e:
            return HttpResponseRedirect(e.response)













        



    

    

    
    
    
   

