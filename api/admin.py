from django.contrib import admin
from .models import Article, Language


class ArticleAdmin(admin.ModelAdmin):
    pass


class LanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Language, LanguageAdmin)
