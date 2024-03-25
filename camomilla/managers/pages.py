from typing import Any, Tuple
from django.db.models.query import QuerySet
from django.db import transaction
from django.apps import apps

URL_NODE_RELATED_NAME = "%(app_label)s_%(class)s"


class PageQuerySet(QuerySet):
    def get_or_create(self, defaults=None, **kwargs) -> Tuple[Any, bool]:
        if "permalink" in kwargs and isinstance(kwargs["permalink"], str):
            if kwargs["permalink"].startswith("/"):
                kwargs["permalink"] = kwargs["permalink"][1:]
            with transaction.atomic():
                UrlNode = apps.get_model("camomilla", "UrlNode")
                url_node, created = UrlNode.objects.get_or_create(
                    defaults={
                        "related_name": URL_NODE_RELATED_NAME
                        % {
                            "app_label": self.model._meta.app_label,
                            "class": self.model._meta.model_name,
                        }
                    },
                    permalink=kwargs["permalink"],

                )
                if created is False and url_node.page is not None:
                    page = self.get(**kwargs)
                    if page.pk != url_node.page.pk:
                        raise self.model.MultipleObjectsReturned(
                            "got more than one %s object for the same permalink: %s"
                            % (
                                self.model._meta.object_name,
                                kwargs["permalink"],
                            )
                        )
                    return url_node.page, False
                kwargs["url_node"] = url_node
                kwargs["slug"] = kwargs["permalink"]
                kwargs.pop("permalink")
                return super().get_or_create(defaults, **kwargs)
        return super().get_or_create(defaults, **kwargs)
