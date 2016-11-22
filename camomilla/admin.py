from django.contrib import admin
from .models import Article, Tag, Category, Content, Media, UserProfile, Page

from hvad.admin import TranslatableAdmin


class PageAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(TranslatableAdmin):
    pass


class TagAdmin(TranslatableAdmin):
    pass


class CategoryAdmin(TranslatableAdmin):
    pass


class ContentAdmin(TranslatableAdmin):
    pass


class MediaAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Page, PageAdmin)
