from django.conf import settings
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .pagination import *
from ...permissions import CamomillaBasePermissions
from django.utils import translation


class GetUserLanguageMixin(object):
    def _get_user_language(self, request):
        self.active_language = request.GET.get(
            "language",
            request.data.get(
                "language_code", translation.get_language_from_request(request)
            ),
        )
        self.language_fallbacks = True
        if (
            len(self.active_language.split("-")) == 2
            and self.active_language.split("-")[0] == "nofallbacks"
        ):
            self.language_fallbacks = False
            self.active_language = self.active_language.split("-")[1]
        translation.activate(self.active_language)
        return self.active_language

    def initialize_request(self, request, *args, **kwargs):
        self._get_user_language(request)
        return super().initialize_request(request, *args, **kwargs)

    def get_queryset(self):
        return (
            self.model.objects.language(self.active_language).fallbacks().all()
            if self.language_fallbacks
            else self.model.objects.language(self.active_language).all()
        )


class BulkDeleteMixin(object):
    @action(detail=False, methods=['post'], permission_classes=(CamomillaBasePermissions,))
    def bulk_delete(self, request):
        try:
            self.model.objects.filter(pk__in=request.data).delete()
            return Response({'detail': 'Eliminazione multipla andata a buon fine' }, status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'Eliminazione multipla non riuscita' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
