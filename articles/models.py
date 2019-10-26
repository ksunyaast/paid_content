from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    subscription = models.BooleanField(default=False, verbose_name='Подписка')


class Article(models.Model):
    title = models.CharField(max_length=3000, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    paid_article = models.BooleanField(default=False, verbose_name='Платная статья')

