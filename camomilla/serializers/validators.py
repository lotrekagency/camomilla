from django.utils.translation import gettext_lazy as _
from modeltranslation.utils import build_localized_fieldname
from rest_framework.exceptions import ValidationError

from camomilla.models.page import UrlNode
from camomilla.utils import activate_languages, is_page
from camomilla.utils.translation import get_nofallbacks, set_nofallbacks


class UniquePermalinkValidator:
    message = _("This slug generates a non-unique permalink.")

    requires_context = True

    def __call__(self, value, serializer):
        if not is_page(serializer.Meta.model):
            return
        errors = {}
        instance = serializer.instance
        exclude_kwargs = {}
        if instance and instance.url_node:
            exclude_kwargs["pk"] = instance.url_node.pk
        parent_page_field = getattr(
            getattr(serializer.Meta.model, "PageMeta", object),
            "parent_page_field",
            "parent_page",
        )
        parent_page = value.get(parent_page_field, None) or getattr(
            instance, parent_page_field, None
        )
        for language in activate_languages():
            f_name = build_localized_fieldname("slug", language)
            slug = value.get(f_name, instance and get_nofallbacks(instance, "slug"))
            fake_instance = serializer.Meta.model()
            set_nofallbacks(fake_instance, "slug", slug)
            if parent_page:
                set_nofallbacks(fake_instance, parent_page_field, parent_page)
            permalink = fake_instance.generate_permalink(safe=False)
            qs = UrlNode.objects.exclude(**exclude_kwargs)
            if qs.filter(permalink=permalink).exists():
                errors[f_name] = self.message
        if len(errors.keys()):
            raise ValidationError(errors)
