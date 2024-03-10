from .models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin


class MainPage(ListView):
    model = Article
    ordering = 'title'
    template_name = 'main.html'
    context_object_name = 'articles'
    paginate_by = 6


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'


class ArticleCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ArticleForm
    model = Article
    template_name = 'article_create.html'


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = ArticleForm
    model = Article
    template_name = 'article_create.html'
