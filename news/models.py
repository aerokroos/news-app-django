from django.db import models

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        full_name = self.first_name.title() + " " + self.last_name.title()
        return full_name

class New(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    section = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.title