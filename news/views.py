from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Article, Reporter, User
from django.urls import reverse_lazy


from .forms import RegisterForm, ReporterForm

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
    succes_url = reverse_lazy('news_home')

class CreateReporterPageView(CreateView):
    model = Reporter
    form_class = ReporterForm
    template_name = 'news/new_reporter.html'
    success_url = reverse_lazy('news_home')

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy('piece-detail', kwargs={'pk': self.kwargs['pk']})

    

    
    
    
   

