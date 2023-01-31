from rest_framework.decorators import action
from rest_framework.response import Response
from camomilla.permissions import CamomillaBasePermissions
from django.core.exceptions import ImproperlyConfigured
from django.db import transaction, router
from django.db.models.signals import post_save, pre_save
from itertools import chain
from django.db.models.expressions import F
from camomilla.fields import ORDERING_ACCEPTED_FIELDS


class OrderingMixin:
    @action(
        detail=False, methods=["post"], permission_classes=(CamomillaBasePermissions,)
    )
    def update_order(self, request):
        startId = int(request.data.get("startId"))
        endId = int(request.data.get("endId"))
        moved_items = list(self.move_item(startId, endId))
        return Response({"moved": moved_items, "reordered": self.reordered})

    @transaction.atomic
    def move_item(self, startId, endId):
        self.reordered = False
        model = self._get_model()
        (
            self.default_order_inverse,
            self.default_order_field,
        ) = self._get_default_ordering(model)
        rank_field = self.default_order_field

        startorder, endorder = self._get_order(startId, endId, model, rank_field)
        if endorder < startorder:
            move_filter = {
                f"{rank_field}__gte": endorder,
                f"{rank_field}__lte": startorder - 1,
            }
            move_delta = +1
            order_by = f"-{rank_field}"
        elif endorder > startorder:
            move_filter = {
                f"{rank_field}__gte": startorder + 1,
                f"{rank_field}__lte": endorder,
            }
            move_delta = -1
            order_by = rank_field
        else:
            return model.objects.none()

        obj_filters = {rank_field: startorder}

        try:
            obj = model.objects.get(**obj_filters)
        except (model.MultipleObjectsReturned, model.DoesNotExist):
            self._reorder(model)
            obj = model.objects.get(**obj_filters)

        move_qs = model.objects.filter(**move_filter).order_by(order_by)
        move_objs = list(move_qs)
        for instance in move_objs:
            setattr(instance, rank_field, getattr(instance, rank_field) + move_delta)
            pre_save.send(
                model,
                instance=instance,
                update_fields=[rank_field],
                raw=False,
                using=router.db_for_write(model, instance=instance),
            )
        move_qs.update(**{rank_field: F(rank_field) + move_delta})
        for instance in move_objs:
            post_save.send(
                model,
                instance=instance,
                update_fields=[rank_field],
                raw=False,
                using=router.db_for_write(model, instance=instance),
                created=False,
            )

        setattr(obj, rank_field, endorder)
        obj.save(update_fields=[rank_field])

        return [
            {"pk": instance.pk, "order": getattr(instance, rank_field)}
            for instance in chain(move_objs, [obj])
        ]

    def _get_default_ordering(self, model=None):
        model = model or self._get_model()
        try:
            _, prefix, field_name = model._meta.ordering[0].rpartition("-")
            model_field = model._meta.get_field(field_name)
            if not isinstance(model_field, ORDERING_ACCEPTED_FIELDS):
                raise ImproperlyConfigured(
                    f"Model {model.__module__}.{model.__name__} has a non-ordinable field '{model_field.__name__}' as first ordering key"
                )
        except (AttributeError, IndexError):
            raise ImproperlyConfigured(
                f"Model {model.__module__}.{model.__name__} requires a list or tuple 'ordering' in its Meta class"
            )
        return prefix == "-", field_name

    def _get_model(self):
        qs = self.get_queryset()
        return getattr(qs, "shared_model", getattr(qs, "model", None))

    def _get_order(self, startId, endId, model, rank_field):
        startorder = getattr(model.objects.get(pk=startId), rank_field)
        endorder = getattr(model.objects.get(pk=endId), rank_field)
        if startorder == endorder:
            self._reorder(model)
            return self._get_order(startId, endId, model, rank_field)
        return startorder, endorder

    def _reorder(self, model):
        self.reordered = True

        order = [
            "-" if self.default_order_inverse else "" + self.default_order_field,
            "pk" if self.default_order_inverse else "-pk",
        ]
        for index, obj in enumerate(model.objects.order_by(*order).iterator()):
            setattr(obj, self.default_order_field, index)
            obj.save()
