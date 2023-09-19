from typing import Any, Callable, Dict, Generic, TypeVar, Union

from django.db import models as django_models
from pydantic import SerializationInfo
from pydantic_core import core_schema as cs

from .utils import get_type


T = TypeVar("T", bound=django_models.Model)


class ForeignKey(Generic[T]):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Any, handler: Callable[[Any], cs.CoreSchema]
    ) -> cs.CoreSchema:
        from camomilla.structured.cache import ValueWithCache

        model_class = get_type(source)

        def validate_from_pk(pk: Union[int, str]) -> model_class:
            return model_class._default_manager.get(pk=pk)

        int_str_union = cs.union_schema([cs.str_schema(), cs.int_schema()])
        from_pk_schema = cs.chain_schema(
            [
                int_str_union,
                cs.no_info_plain_validator_function(validate_from_pk),
            ]
        )
        pk_attname = model_class._meta.pk.attname

        def validate_from_dict(data: Dict[str, Union[str, int]]) -> model_class:
            return validate_from_pk(data[pk_attname])

        from_dict_schema = cs.chain_schema(
            [
                cs.typed_dict_schema({pk_attname: cs.typed_dict_field(int_str_union)}),
                cs.no_info_plain_validator_function(validate_from_dict),
            ]
        )

        from_cache_schema = cs.chain_schema(
            [
                cs.is_instance_schema(ValueWithCache),
                cs.no_info_plain_validator_function(lambda v: v.retrieve()),
            ]
        )

        def serialize_data(instance, info):
            from camomilla.serializers.utils import build_standard_model_serializer

            if info.mode == "python":
                serializer = build_standard_model_serializer(model_class, depth=1)
                return serializer(instance=instance).data
            return instance.pk

        return cs.json_or_python_schema(
            json_schema=cs.union_schema(
                [from_cache_schema, from_pk_schema, from_dict_schema]
            ),
            python_schema=cs.union_schema(
                [
                    cs.is_instance_schema(model_class),
                    from_cache_schema,
                    from_pk_schema,
                    from_dict_schema,
                ]
            ),
            serialization=cs.plain_serializer_function_ser_schema(
                serialize_data, info_arg=True
            ),
        )


class QuerySet(Generic[T]):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Any, handler: Callable[[Any], cs.CoreSchema]
    ) -> cs.CoreSchema:
        from camomilla.structured.cache import ValueWithCache

        model_class = get_type(source)

        def validate_from_pk_list(
            values: list[Union[int, str]]
        ) -> django_models.QuerySet:
            preserved = django_models.Case(
                *[django_models.When(pk=pk, then=pos) for pos, pk in enumerate(values)]
            )
            return model_class._default_manager.filter(pk__in=values).order_by(
                preserved
            )

        int_str_union = cs.union_schema([cs.str_schema(), cs.int_schema()])
        from_pk_list_schema = cs.chain_schema(
            [
                cs.list_schema(int_str_union),
                cs.no_info_plain_validator_function(validate_from_pk_list),
            ]
        )
        pk_attname = model_class._meta.pk.attname

        def validate_from_dict(
            values: list[Dict[str, Union[str, int]]]
        ) -> django_models.QuerySet:
            return validate_from_pk_list([data[pk_attname] for data in values])

        from_dict_list_schema = cs.chain_schema(
            [
                cs.list_schema(
                    cs.typed_dict_schema(
                        {pk_attname: cs.typed_dict_field(int_str_union)}
                    )
                ),
                cs.no_info_plain_validator_function(validate_from_dict),
            ]
        )
        from_cache_schema = cs.chain_schema(
            [
                cs.is_instance_schema(ValueWithCache),
                cs.no_info_plain_validator_function(lambda v: v.retrieve()),
            ]
        )

        def serialize_data(qs: django_models.QuerySet, info: SerializationInfo):
            from camomilla.serializers.utils import build_standard_model_serializer

            if info.mode == "python":
                serializer = build_standard_model_serializer(model_class, depth=1)
                return serializer(instance=qs, many=True).data
            return [x.pk for x in qs]

        return cs.json_or_python_schema(
            json_schema=cs.union_schema(
                [from_cache_schema, from_pk_list_schema, from_dict_list_schema]
            ),
            python_schema=cs.union_schema(
                [
                    cs.is_instance_schema(django_models.QuerySet),
                    from_cache_schema,
                    from_pk_list_schema,
                    from_dict_list_schema,
                ]
            ),
            serialization=cs.plain_serializer_function_ser_schema(
                serialize_data, info_arg=True
            ),
        )
