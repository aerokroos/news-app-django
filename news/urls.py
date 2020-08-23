from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsPageView.as_view(), name='news_home'),
    path('reporter/<int:pk>/', views.ReporterPageView.as_view(), name="reporter_view"),
    path('signup/', views.SignupCreatePage.as_view(), name='signup'),
    path('new_reporter/', views.CreateReporterPageView.as_view(), name='new_reporter')
]