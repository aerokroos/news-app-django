from django.db import models

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        full_name = self.first_name.title() + " " + self.last_name.title()
        return full_name

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
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return '#'