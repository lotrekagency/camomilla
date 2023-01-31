from typing import Any, Iterable, Iterator

from django.db.models import Model
from django.utils.translation.trans_real import activate, get_language
from modeltranslation.settings import AVAILABLE_LANGUAGES
from modeltranslation.utils import build_localized_fieldname


def activate_languages(languages: Iterable[str] = AVAILABLE_LANGUAGES) -> Iterator[str]:
    old = get_language()
    for language in languages:
        activate(language)
        yield language
    activate(old)


def set_nofallbacks(instance: Model, attr: str, value: Any) -> None:
    local_fieldname = build_localized_fieldname(attr, get_language())
    if hasattr(instance, local_fieldname):
        attr = local_fieldname
    return setattr(instance, attr, value)


def get_nofallbacks(instance: Model, attr: str, *args, **kwargs) -> Any:
    local_fieldname = build_localized_fieldname(attr, get_language())
    if hasattr(instance, local_fieldname):
        attr = local_fieldname
    return getattr(instance, attr, *args, **kwargs)
