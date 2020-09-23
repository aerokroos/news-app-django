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
    
    
]