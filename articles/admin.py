from django.contrib import admin
from .models import Profile, Article


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'subscription')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'paid_article')