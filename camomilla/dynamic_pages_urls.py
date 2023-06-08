from django.shortcuts import render
from django.urls import path

from .models import Page, UrlNode


def fetch(request, *args, **kwargs):
    if "permalink" in kwargs:
        page = Page.get_or_404(request)
    else:
        try:
            page = Page.get(request, bypass_type_check=True)
        except UrlNode.DoesNotExist:
            page, _ = Page.get_or_create(request, slug="")
    return render(request, page.template_name, {"page": page, "page_extra": {"class": page.__class__.__name__, "module": page.__module__} })


urlpatterns = [
    path("", fetch, name="camomilla-homepage"),
    path("<path:permalink>", fetch, name="camomilla-catch-em-all"),
]
