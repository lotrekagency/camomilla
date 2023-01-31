from modeltranslation.translator import TranslationOptions, register

from camomilla.models import Article, Content, Media, Page, Tag, UrlNode


class SeoMixinTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "description",
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
    fields = ("name",)


@register(Content)
class ContentTranslationOptions(TranslationOptions):
    fields = ("content",)
    empty_values = {"title": None}


@register(Media)
class MediaTranslationOptions(TranslationOptions):
    fields = ("title_tag", "alt_tag", "description_tag")


@register(Page)
class PageTranslationOptions(SeoMixinTranslationOptions):
    fields = ("breadcrumbs_title", "slug", "status", "indexable")


@register(UrlNode)
class UrlNodeTranslationOptions(TranslationOptions):
    fields = ("permalink",)
