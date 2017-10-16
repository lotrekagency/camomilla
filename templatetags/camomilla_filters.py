from django import template

register = template.Library()


@register.filter(name='filter_object')
def filter_object(objects, args):
    value, attr = args.split(',')
    for obj in objects:
        if getattr(obj, attr, None) == value:
            return obj


@register.filter(name='filter_content')
def filter_content(objects, args):
    return filter_object(objects, args + ',identifier')