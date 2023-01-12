from modeltranslation.translator import register, TranslationOptions
from .models import Article, Tag, Category, Content, Media, Page, MediaFolder


class SeoMixinTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
        "permalink",
        "og_description",
        "og_title",
        "og_type",
        "og_url",
        "canonical",
    )


@register(Article)
class ArticleTranslationOptions(SeoMixinTranslationOptions):
    fields = ("content",)
    empty_values = {"permalink": None}


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("title", "description", "slug")


@register(Content)
class ContentTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "permalink", "content")
    empty_values = {"title": None}


@register(MediaFolder)
class MediaFolderTranslationOptions(TranslationOptions):
    fields = ("title", "description")


@register(Media)
class MediaTranslationOptions(TranslationOptions):
    fields = ("title", "description", "alt_text")


@register(Page)
class PageTranslationOptions(SeoMixinTranslationOptions):
    pass
