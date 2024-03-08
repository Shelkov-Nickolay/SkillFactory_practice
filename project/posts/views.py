from .models import Article
from django.views.generic import ListView


class MainPage(ListView):
    model = Article
    ordering = 'title'
    template_name = 'main.html'
    context_object_name = 'articles'
