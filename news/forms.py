from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reporter, Article

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ["first_name", "last_name","username", "email", "password1", "password2"]

class ReporterForm(forms.ModelForm):
    
    class Meta:
        model = Reporter
        fields = '__all__'
        exclude = ['reporter']
        #widgets = {"user": forms.HiddenInput()}

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['article_reporter']
        
        
