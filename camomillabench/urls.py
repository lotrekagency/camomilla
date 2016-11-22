from django.contrib import admin

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from camomilla.views import CamomillaObtainAuthToken


admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    url(r'^{0}/'.format(getattr(settings, 'ADMIN_URL', 'admin')), admin.site.urls),
    url(r'^api-token-auth/', CamomillaObtainAuthToken.as_view()),
    url(r'^api/', include('camomilla.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

try:
    urlpatterns = [
        url(r'^{0}/'.format(settings.ULR_PREFIX), include(urlpatterns)),
    ]
except AttributeError as ex:
    pass
