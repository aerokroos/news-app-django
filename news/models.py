from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.auth import get_user_model
#from .urls import *

# Create your models here.
class Reporter(models.Model):
    reporter = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='reporters/',null=True, blank=True)
    website = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.reporter.username

class Section(models.Model):
    name_section = models.CharField(max_length=30)

    def __str__(self):
        return self.name_section.title()

class Article(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)

    def __str__(self):
        return self.title
    
# class User(AbstractUser):
#     pass





    