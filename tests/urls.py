from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns


def dummy_view(request):
    from django.http import HttpResponse

    return HttpResponse("Here's the text of the Web page.")


urlpatterns = [
    path("articles/<slug:title>", dummy_view, name="article-detail"),
    path("api/camomilla/", include("camomilla.urls")),
]


urlpatterns += i18n_patterns(
    path("about", dummy_view, name="about"),
    path("international_articles/<slug:title>", dummy_view, name="int-article-detail"),
    prefix_default_language=False,
)
