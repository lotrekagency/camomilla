from django.conf import settings
from rest_framework.response import Response
from rest_framework import views


class LanguageViewSet(views.APIView):
    def get(self, request, *args, **kwargs):
        languages = []
        for key, language in settings.LANGUAGES:
            languages.append({"id": key, "name": language})
        return Response(
            {"language_code": settings.LANGUAGE_CODE, "languages": languages}
        )
