from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from rest_framework_jwt.views import obtain_jwt_token



def dummy_view(request):
    from django.http import HttpResponse
    return HttpResponse("Here's the text of the Web page.")

urlpatterns = [
    path('articles/<slug:title>', dummy_view, name='article-detail'),

    path('api/camomilla/', include('camomilla.urls')),

    path("api/api-token-auth/", obtain_jwt_token),
]


urlpatterns += i18n_patterns(
    path('about', dummy_view, name='about'),
    path('international_articles/<slug:title>', dummy_view, name='int-article-detail'),
    prefix_default_language=False
)
