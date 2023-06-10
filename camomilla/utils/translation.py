import re
from typing import Any, Iterable, Iterator

from django.db.models import Model, Q
from django.utils.translation.trans_real import activate, get_language
from modeltranslation.settings import AVAILABLE_LANGUAGES, DEFAULT_LANGUAGE
from modeltranslation.utils import build_localized_fieldname


def activate_languages(languages: Iterable[str] = AVAILABLE_LANGUAGES) -> Iterator[str]:
    old = get_language()
    for language in languages:
        activate(language)
        yield language
    activate(old)


def set_nofallbacks(instance: Model, attr: str, value: Any, **kwargs) -> None:
    language = kwargs.pop("language", get_language())
    local_fieldname = build_localized_fieldname(attr, language)
    if hasattr(instance, local_fieldname):
        attr = local_fieldname
    return setattr(instance, attr, value)


def get_nofallbacks(instance: Model, attr: str, *args, **kwargs) -> Any:
    language = kwargs.pop("language", get_language())
    local_fieldname = build_localized_fieldname(attr, language)
    if hasattr(instance, local_fieldname):
        attr = local_fieldname
    return getattr(instance, attr, *args, **kwargs)


def url_lang_decompose(url):
    data = {"url": url, "permalink": url, "language": DEFAULT_LANGUAGE}
    result = re.match(f"^\/?({'|'.join(AVAILABLE_LANGUAGES)})?\/(.*)", url).groups()
    if result and len(result) == 2:
        data["language"] = result[0]
        data["permalink"] = "/%s" % result[1]
    return data


def get_field_translations(instance: Model, field_name: str, *args, **kwargs):
    return {
        lang: get_nofallbacks(instance, field_name, language=lang, *args, **kwargs)
        for lang in AVAILABLE_LANGUAGES
    }


def lang_fallback_query(**kwargs):
    current_lang = get_language()
    query = Q()
    for lang in AVAILABLE_LANGUAGES:
        query |= Q(**{f"{key}_{lang}": value for key, value in kwargs.items()})
    if current_lang:
        query = (query & Q(**{f"{key}_{current_lang}__isnull": True for key in kwargs.keys()}))
        query |= Q(**{f"{key}_{current_lang}": value for key, value in kwargs.items()})
    return query
