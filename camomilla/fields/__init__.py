from django.db import models

from camomilla.structured import StructuredJSONField

from .json import ArrayField, JSONField

ORDERING_ACCEPTED_FIELDS = (
    models.BigIntegerField,
    models.IntegerField,
    models.PositiveIntegerField,
    models.PositiveSmallIntegerField,
    models.SmallIntegerField,
)

__all__ = ["StructuredJSONField", "JSONField", "ArrayField", "ORDERING_ACCEPTED_FIELDS"]
