from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.sites import AlreadyRegistered
from .models import Article, Tag, Category, Content, Media, SitemapUrl

from hvad.admin import TranslatableAdmin


class CamomillaUserAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(TranslatableAdmin):
    exclude = ('author',)
    #readonly_fields = ('slug',)


class TagAdmin(TranslatableAdmin):
    #readonly_fields = ('slug',)
    pass


class CategoryAdmin(TranslatableAdmin):
    pass


class ContentAdmin(TranslatableAdmin):
    exclude = ('author',)


class MediaAdmin(TranslatableAdmin):
    exclude = ('thumbnail', 'size', 'is_image')
    readonly_fields = ('image_preview', 'image_thumb_preview')
    list_display = ('__str__', 'name', 'image_thumb_preview',)


class SitemapUrlAdmin(TranslatableAdmin):
    pass


try:
    admin.site.register(get_user_model(), CamomillaUserAdmin)
except AlreadyRegistered:
    raise Exception ('You need to define your own AUTH_USER_MODEL. Please follow the README.md')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(SitemapUrl, SitemapUrlAdmin)
