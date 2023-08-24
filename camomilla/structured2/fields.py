from typing import Any, Callable, Dict, Generic, TypeVar, Union

from django.core.exceptions import ImproperlyConfigured
from django.db import models as django_models
from pydantic_core import core_schema
from typing_extensions import get_args

T = TypeVar("T", bound=django_models.Model)


class ForeignKey(django_models.Model, Generic[T]):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Any, handler: Callable[[Any], core_schema.CoreSchema]
    ) -> core_schema.CoreSchema:
        try:
            model_class = get_args(source)[0]
        except IndexError:
            raise ImproperlyConfigured(
                "Must provide a Model class for ForeignKey fields."
            )

        def validate_from_pk(pk: Union[int, str]) -> model_class:
            return model_class._default_manager.get(pk=pk)

        int_str_union = core_schema.union_schema(
            [core_schema.str_schema(), core_schema.int_schema()]
        )
        from_pk_schema = core_schema.chain_schema(
            [
                int_str_union,
                core_schema.no_info_plain_validator_function(validate_from_pk),
            ]
        )
        pk_attname = model_class._meta.pk.attname

        def validate_from_dict(data: Dict[str, Union[str, int]]) -> model_class:
            return model_class._default_manager.get(pk=data[pk_attname])

        from_dict_schema = core_schema.chain_schema(
            [
                core_schema.typed_dict_schema(
                    {pk_attname: core_schema.typed_dict_field(int_str_union)}
                ),
                core_schema.no_info_plain_validator_function(validate_from_dict),
            ]
        )

        return core_schema.json_or_python_schema(
            json_schema=core_schema.union_schema([from_pk_schema, from_dict_schema]),
            python_schema=core_schema.union_schema(
                [
                    core_schema.is_instance_schema(model_class),
                    from_pk_schema,
                    from_dict_schema,
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda instance: instance.pk
            ),
        )


class QuerySet(Generic[T]):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Any, handler: Callable[[Any], core_schema.CoreSchema]
    ) -> core_schema.CoreSchema:
        try:
            model_class = get_args(source)[0]
        except IndexError:
            raise ImproperlyConfigured(
                "Must provide a Model class for QuerySet fields."
            )

        def validate_from_pk_list(
            values: list[Union[int, str]]
        ) -> django_models.QuerySet:
            preserved = django_models.Case(
                *[django_models.When(pk=pk, then=pos) for pos, pk in enumerate(values)]
            )
            return model_class._default_manager.filter(pk__in=values).order_by(
                preserved
            )

        int_str_union = core_schema.union_schema(
            [core_schema.str_schema(), core_schema.int_schema()]
        )
        from_pk_list_schema = core_schema.chain_schema(
            [
                core_schema.list_schema(int_str_union),
                core_schema.no_info_plain_validator_function(validate_from_pk_list),
            ]
        )
        pk_attname = model_class._meta.pk.attname

        def validate_from_dict(
            values: list[Dict[str, Union[str, int]]]
        ) -> django_models.QuerySet:
            return validate_from_pk_list([data[pk_attname] for data in values])

        from_dict_list_schema = core_schema.chain_schema(
            [
                core_schema.list_schema(
                    core_schema.typed_dict_schema(
                        {pk_attname: core_schema.typed_dict_field(int_str_union)}
                    )
                ),
                core_schema.no_info_plain_validator_function(validate_from_dict),
            ]
        )

        return core_schema.json_or_python_schema(
            json_schema=core_schema.union_schema(
                [from_pk_list_schema, from_dict_list_schema]
            ),
            python_schema=core_schema.union_schema(
                [
                    core_schema.is_instance_schema(django_models.QuerySet),
                    from_pk_list_schema,
                    from_dict_list_schema,
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda qs: list(qs.values_list("pk", flat=True))
            ),
        )
