from django.shortcuts import render
from django.urls import path

from .models import AbstractPage


def fetch(request, *args, **kwargs):
    if "permalink" in kwargs:
        page = AbstractPage.get_or_404(request)
    else:
        page, _ = AbstractPage.get_or_create_homepage()
    return render(request, page.template_name, {"page": page, "page_extra": {"class": page.__class__.__name__, "module": page.__module__} })


urlpatterns = [
    path("", fetch, name="camomilla-homepage"),
    path("<path:permalink>", fetch, name="camomilla-catch-em-all"),
]
