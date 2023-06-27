from django.shortcuts import render
from django.urls import path

from .models import Page


def fetch(request, *args, **kwargs):
    if "permalink" in kwargs:
        page = Page.get_or_404(request, bypass_type_check=True)
    else:
        page, _ = Page.get_or_create_homepage()
    return render(request, page.get_template_path(request), page.get_context(request))


urlpatterns = [
    path("", fetch, name="camomilla-homepage"),
    path("<path:permalink>", fetch, name="camomilla-catch-em-all"),
]
