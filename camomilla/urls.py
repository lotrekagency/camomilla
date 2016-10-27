from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import include, url
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api/', include('api.urls')),
]
