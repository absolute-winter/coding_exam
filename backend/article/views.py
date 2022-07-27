from ast import Del
from pyexpat import model
from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ArticleList(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'article/index.html'

class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'article/create.html'
    success_url = reverse_lazy('index')

class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'article/detail.html'

class ArticleEdit(UpdateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'article/edit.html'
    success_url = reverse_lazy('index')

class ArticleDelete(DeleteView):
    model = Article
    context_object_name = 'article'
    template_name = 'article/delete.html'
    success_url = reverse_lazy('index')