from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsPageView.as_view(), name='news_home'),
    path('reporter/<int:pk>/', views.ReporterPageView.as_view(), name="reporter_view"),
    path('signup/', views.SignupCreatePage.as_view(), name='signup'),
    path('new_reporter/', views.CreateReporterPageView.as_view(), name='new_reporter'),
    path('new_article/', views.CreateArticlePageView.as_view(), name='new_article'),
    path('education/', views.EducationPageView.as_view(), name='education'),
    path('sports/', views.SportsPageView.as_view(), name='sports'),
    path('politics/', views.PoliticsPageView.as_view(), name='politics'),
    path('science/', views.SciencePageView.as_view(), name='science'),
    path('entertainment/', views.EntertainmentPageView.as_view(), name='entertainment'),
    path('technology/', views.TechnologyPageView.as_view(), name='technology'),
    path('economy/', views.EconomyPageView.as_view(), name='economy'),
    path('arts/', views.ArtsPageView.as_view(), name='arts'),
    path('weather/', views.WeatherPageView.as_view(), name='weather'),
    path('fasion/', views.FashionPageView.as_view(), name='fashion'),
    path('health/', views.HealthPageView.as_view(), name='health'),
    path('results/', views.SearchView.as_view(), name='search'),
    path('article/<int:pk>/', views.ArticlePageView.as_view(), name='article_view'),
]