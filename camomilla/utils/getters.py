from typing import Any, Callable, Union


def safe_getter(instance: Union[dict, object], key: str, default: Any = None) -> Any:
    if isinstance(instance, dict):
        return instance.get(key, default)
    return getattr(instance, key, default)


def pointed_getter(
    instance: Union[dict, object], pointed: str, default: Any = None
) -> Any:
    attrs = pointed.split(".", 1)
    data = safe_getter(instance, attrs[0], default)
    if len(attrs) == 2:
        data = pointed_getter(data, attrs[1], default)
    return data


def find_and_replace_dict(obj: dict, predicate: Callable):
    result = {}
    for k, v in obj.items():
        v = predicate(key=k, value=v)
        if isinstance(v, dict):
            v = find_and_replace_dict(v, predicate)
        result[k] = v
    return result
