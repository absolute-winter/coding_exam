from turtle import title
from django.db import models
from django.forms import DateField

class Article(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    createdDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title