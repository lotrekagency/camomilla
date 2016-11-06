from django.contrib import admin

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from camomilla.views import CamomillaObtainAuthToken


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', CamomillaObtainAuthToken.as_view()),
    url(r'^api/', include('camomilla.urls')),
    url(r'^profileslist/', include('plugin_profileslist.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
