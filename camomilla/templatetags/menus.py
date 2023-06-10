from django import template
from camomilla.models import Menu
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.simple_tag(takes_context=True)
def get_menus(context, *args):
    if "menus" in context:
        return context["menus"]
    qs = Menu.objects.all()
    if len(args):
        qs = qs.filter(key__in=args)
    return Menu.defaultdict({m.key: m for m in qs})


@register.filter(name="node_url")
def get_menu_node_url(node):
    link = node.get("link", {})
    link_type = link.get("link_type", None)
    if link_type == "RE":
        # TODO: increase performances of this:
        rel = link.get("relational")
        c_type = ContentType.objects.filter(pk=rel["content_type"]).first()
        model = c_type and c_type.model_class()
        page = model and model.objects.filter(pk=rel.get("page_id")).first()
        return getattr(page, "permalink", None)
    elif link_type == "ST":
        return link.get("static", None)
