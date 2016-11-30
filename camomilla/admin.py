from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Article, Tag, Category, Content, Media, SitemapUrl

from hvad.admin import TranslatableAdmin


class CamomillaUserAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(TranslatableAdmin):
    exclude = ('author',)


class TagAdmin(TranslatableAdmin):
    pass


class CategoryAdmin(TranslatableAdmin):
    pass


class ContentAdmin(TranslatableAdmin):
    exclude = ('author',)


class MediaAdmin(TranslatableAdmin):
    exclude = ('thumbnail', 'size', 'is_image')


class SitemapUrlAdmin(TranslatableAdmin):
    pass


admin.site.register(get_user_model(), CamomillaUserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(SitemapUrl, SitemapUrlAdmin)
