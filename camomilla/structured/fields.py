import datetime
import decimal

from django.core import validators
from django.db import models
from django.utils.dateparse import parse_duration
from django.utils.duration import duration_string
from jsonmodels import fields
from jsonmodels.validators import ValidationError
from camomilla.utils.getters import pointed_getter


__all__ = [
    "CharField",
    "DecimalField",
    "IntegerField",
    "FloatField",
    "BooleanField",
    "DateTimeField",
    "DateField",
    "TimeField",
    "DurationField",
    "EmailField",
    "SlugField",
    "URLField",
    "ListField",
    "DictField",
    "EmbeddedField",
    "ForeignKey",
    "ForeignKeyList",
]


class Field(fields.BaseField):
    additional_kwargs = {}
    additional_validators = []
    __validators = []
    parent = None

    def __init__(self, *args, **kwargs):
        for key, value in self.additional_kwargs.items():
            setattr(self, key, kwargs.pop(key, value))
        super(Field, self).__init__(*args, **kwargs)

    @property
    def validators(self):
        validators = self.__validators
        for validator in self.additional_validators:
            if isinstance(validator, dict):
                validator_class = validator["validator"]
                args = [
                    getattr(self, arg)
                    for arg in validator.get("args", [])
                    if getattr(self, arg, fields.NotSet) != fields.NotSet
                ]
                kwargs = {
                    key: getattr(self, value)
                    for key, value in validator.get("kwargs", {}).items()
                    if getattr(self, value, fields.NotSet) != fields.NotSet
                }
                if len(args) or len(kwargs.keys()):
                    validators.append(validator_class(*args, **kwargs))
            else:
                validators.append(validator)
        return validators

    @validators.setter
    def validators(self, value):
        self.__validators = value

    def bind(self, parent):
        self.parent = parent

    @classmethod
    def to_db_transform(cls, data):
        return data

    @classmethod
    def from_db_transform(cls, data):
        return data


class CharField(fields.StringField, Field):
    additional_kwargs = {
        "max_length": fields.NotSet,
    }
    additional_validators = [
        {"validator": validators.MaxLengthValidator, "args": ["max_length"]}
    ]


class DecimalField(fields.StringField, Field):
    types = (decimal.Decimal, int, float)

    additional_kwargs = {
        "max_digits": fields.NotSet,
        "decimal_places": fields.NotSet,
    }
    additional_validators = [
        {
            "validator": validators.DecimalValidator,
            "args": ["max_digits", "decimal_places"],
        }
    ]


class IntegerField(fields.IntField, Field):
    additional_kwargs = {
        "min_value": fields.NotSet,
        "max_value": fields.NotSet,
    }
    additional_validators = [
        {"validator": validators.MinValueValidator, "args": ["min_value"]},
        {"validator": validators.MaxValueValidator, "args": ["max_value"]},
    ]


class FloatField(IntegerField):
    types = (float, int)


class BooleanField(fields.BoolField, Field):
    pass


class DateTimeField(fields.DateTimeField, Field):
    pass


class DateField(fields.DateField, Field):
    pass


class TimeField(fields.TimeField, Field):
    pass


class DurationField(fields.StringField, Field):
    types = (datetime.timedelta,)

    def to_struct(self, value):
        return value and duration_string(value)

    def parse_value(self, value):
        if value is None:
            return value
        if isinstance(value, datetime.timedelta):
            return value
        try:
            parsed = parse_duration(value)
        except ValueError:
            pass
        else:
            if parsed is not None:
                return parsed

        raise fields.ValidationError(
            f"“{value}” value has an invalid format. It must be in '[DD] [[HH:]MM:]ss[.uuuuuu] format.'"
        )


class EmailField(CharField):
    additional_validators = [validators.validate_email]


class SlugField(CharField):
    additional_validators = [validators.validate_slug]


class URLField(CharField):
    additional_validators = [validators.URLValidator()]


class ListField(fields.ListField, Field):
    def parse_value(self, values):
        """Cast value to proper collection."""
        result = self.get_default_value()
        if not values:
            return result
        if not isinstance(values, list):
            return values
        parent = self.parent
        return [self._cast_value(value, parent) for value in values]

    def _cast_value(self, value, parent):
        if isinstance(value, self.items_types):
            return value
        else:
            main_type = self._get_main_type()
            from camomilla.structured.models import Model

            if issubclass(main_type, Model):
                instance = main_type()
                relations = instance.prepopulate(**value)
                instance.bind(parent)
                instance.populate(**relations)
                return instance
            return main_type(**value)

    def _get_main_type(self):
        if len(self.items_types) != 1:
            raise ValidationError(
                'Cannot decide which type to choose from "{items_types}".'.format(
                    items_types=", ".join([t.__name__ for t in self.items_types])
                )
            )
        return self.items_types[0]


class DictField(fields.DictField, Field):
    pass


class EmbeddedField(fields.EmbeddedField, Field):
    def parse_value(self, value):
        if not isinstance(value, dict):
            return value
        embed_instance = self._get_embed_type()()
        relations = embed_instance.prepopulate(**value)
        embed_instance.bind(self.parent)
        embed_instance.populate(**relations)
        return embed_instance


class ForeignKey(Field):
    types = (models.Model, int, str)

    def __init__(self, to, *args, **kwargs):
        self.model = to
        self.queryset = kwargs.pop("queryset", None)
        super(ForeignKey, self).__init__(*args, **kwargs)

    def get_queryset(self):
        return self.queryset or self.model.objects.all()

    def to_struct(self, value):
        return getattr(value, "pk", value)

    def parse_value(self, value):
        try:
            if isinstance(value, bool):
                raise TypeError
            if isinstance(value, self.model):
                return value
            cache = pointed_getter(self, "parent.get_prefetched_data", lambda: None)()
            if cache is not None:
                return cache.get(self.model, {}).get(value)
            return value and self.get_queryset().get(pk=value)
        except (TypeError, ValueError):
            raise fields.ValidationError(
                "Incorrect type. Expected pk value, received {data_type}.".format(
                    data_type=type(value).__name__
                )
            )


class ForeignKeyList(ListField):
    types = (list, models.QuerySet)

    def __init__(self, to, *args, **kwargs):
        self.inner_model = to
        self.inner_queryset = kwargs.pop("queryset", None)
        kwargs["items_types"] = to
        super(ForeignKeyList, self).__init__(*args, **kwargs)

    def parse_value(self, values):
        result = self.get_default_value()
        if not values:
            return result
        if not isinstance(values, list):
            return values
        cache = pointed_getter(self, "parent.get_prefetched_data", lambda: None)()
        if cache is not None:
            data = cache.get(self.inner_model)
            qs = self.get_inner_queryset().filter(pk__in=values)
            setattr(
                qs,
                "_result_cache",
                [data[i] for i in values if i in data] if data else [],
            )
            return qs
        preserved = models.Case(
            *[models.When(pk=pk, then=pos) for pos, pk in enumerate(values)]
        )
        return self.get_inner_queryset().filter(pk__in=values).order_by(preserved)

    def get_inner_queryset(self):
        return self.inner_queryset or self.inner_model._default_manager.all()

    def to_struct(self, value):
        return [getattr(v, "pk", v) for v in value]
