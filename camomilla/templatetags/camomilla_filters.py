from django import template

register = template.Library()


@register.filter(name='filter_object')
def filter_object(objects, args):
    value, attr = args.split(',')
    for obj in objects:
        if getattr(obj, attr, None) == value:
            return obj


@register.filter(name='filter_content')
def filter_content(page, args):
    try:
        content = page.contents.get(identifier=args)
    except page.contents.model.DoesNotExist:
        content = page.contents.create(identifier=args, title='')
    return content


@register.filter(name='alternate_urls')
def alternate_urls(page, request):
    alternates = page.alternate_urls(request)
    if not alternates or len(alternates.keys()) == 1:
        alternates = {}
    return alternates.get('alternate_urls', alternates).items()
