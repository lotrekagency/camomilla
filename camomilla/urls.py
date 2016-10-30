from django.contrib import admin

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from api.views import CamomillaObtainAuthToken


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', CamomillaObtainAuthToken.as_view()),
    url(r'^api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
