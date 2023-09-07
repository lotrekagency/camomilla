from django.shortcuts import render
from django.urls import path

from camomilla import settings

from .models import Page


def fetch(request, *args, **kwargs):
    preview = request.user.is_staff and request.GET.get("preview", False)
    if "permalink" in kwargs:
        page = Page.get_or_404(
            request, bypass_public_check=preview, bypass_type_check=True
        )
    elif settings.AUTO_CREATE_HOMEPAGE is False:
        page, _ = Page.get_or_404(permalink="/", bypass_type_check=True)
    else:
        page, _ = Page.get_or_create_homepage()
    return render(request, page.get_template_path(request), page.get_context(request))


urlpatterns = [
    path("", fetch, name="camomilla-homepage"),
    path("<path:permalink>", fetch, name="camomilla-permalink"),
]
