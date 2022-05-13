from django import template
from django.utils.translation import get_language


register = template.Library()


@register.filter(name="filter_content")
def filter_content(page, args):
    curr_lang = get_language()
    try:
        content = page.contents.language(curr_lang).get(identifier=args)
    except page.contents.model.DoesNotExist:
        content, _ = page.contents.get_or_create(identifier=args)
    if curr_lang not in content.translations.all_languages():
        content.translate(curr_lang)
        content.save()
    return content


@register.filter(name="alternate_urls")
def alternate_urls(page, request):
    alternates = page.alternate_urls(request)
    return alternates.get("alternate_urls", alternates).items()
