from django.contrib import admin
from .models import Article, Tag, Category, Content, Media, UserProfile, SitemapUrl

from hvad.admin import TranslatableAdmin


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


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(SitemapUrl, SitemapUrlAdmin)
