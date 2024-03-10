from django.urls import path
from .views import MainPage, ArticleDetail, ArticleCreate, ArticleUpdate


urlpatterns = [
    path('', MainPage.as_view()),
    path('<int:pk>', (ArticleDetail.as_view()), name='post_detail'),
    path('create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
]
