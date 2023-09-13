from typing import Any, Generic, Sequence
from typing_extensions import TypeVar, get_args
from django.core.exceptions import ImproperlyConfigured
from camomilla.utils.getters import pointed_getter


T = TypeVar("T")


class _LazyType:
    def __init__(self, path):
        self.path = path

    def evaluate(self, base_cls):
        module, type_name = self._evaluate_path(self.path, base_cls)
        return self._import(module, type_name)

    def _evaluate_path(self, relative_path, base_cls):
        base_module = base_cls.__module__

        modules = self._get_modules(relative_path, base_module)

        type_name = modules.pop()
        module = ".".join(modules)
        if not module:
            module = base_module
        return module, type_name

    def _get_modules(self, relative_path, base_module):
        canonical_path = relative_path.lstrip(".")
        canonical_modules = canonical_path.split(".")

        if not relative_path.startswith("."):
            return canonical_modules

        parents_amount = len(relative_path) - len(canonical_path)
        parent_modules = base_module.split(".")
        parents_amount = max(0, parents_amount - 1)
        if parents_amount > len(parent_modules):
            raise ValueError(f"Can't evaluate path '{relative_path}'")
        return parent_modules[: parents_amount * -1] + canonical_modules

    def _import(self, module_name, type_name):
        module = __import__(module_name, fromlist=[type_name])
        try:
            return getattr(module, type_name)
        except AttributeError:
            raise ValueError(f"Can't find type '{module_name}.{type_name}'.")


def get_type(source: Generic[T], raise_exception=True) -> T:
    try:
        return get_args(source)[0]
    except IndexError:
        if raise_exception:
            raise ImproperlyConfigured(
                "Must provide a Model class for ForeignKey fields."
            )
        else:
            return None


def get_type_eval(source: Generic[T], model: Any, raise_exception=True) -> T:
    type = get_type(source, raise_exception)
    if isinstance(type, str):
        return _LazyType(type).evaluate(model)


def set_key(data, key, val):
    if isinstance(data, Sequence):
        key = int(key)
        if key < len(data):
            data[key] = val
        else:
            data.append(val)
        return data
    elif isinstance(data, dict):
        data[key] = val
    else:
        setattr(data, key, val)
    return data


def get_key(data, key, default):
    if isinstance(data, Sequence):
        try:
            return data[int(key)]
        except IndexError:
            return default
    return pointed_getter(data, key, default)


def pointed_setter(data, path, value):
    path = path.split(".")
    key = path.pop(0)
    if not len(path):
        return set_key(data, key, value)
    default = [] if path[0].isdigit() else {}
    return set_key(
        data, key, pointed_setter(get_key(data, key, default), ".".join(path), value)
    )


def map_method_aliases(new_cls):
    method_aliases = {
        "validate_python": "model_validate",
        "validate_json": "model_validate_json",
        # "dump_python": "model_dump",
        # "dump_json": "model_dump_json",
        "json_schema": "model_json_schema",
    }
    for alias_name, target_name in method_aliases.items():
        setattr(new_cls, alias_name, getattr(new_cls, target_name))
    return new_cls
