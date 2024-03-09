from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    CAT = (
        ('tank', 'Танк'),
        ('heal', 'Медик'),
        ('dd', 'Урон'),
        ('buyers', 'Торговец'),
        ('gildemaster', 'Гилдмастер'),
        ('quest', 'Квестгивер'),
        ('smith', 'Кузнец'),
        ('tanner', 'Кожевник'),
        ('potion', 'Зельевар'),
        ('spellmaster', 'Мастер заклинаний'),
    )

    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=32, choices=CAT, default='dd')
    upload = models.FileField(upload_to='uploads/')
