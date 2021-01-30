from django.conf import settings
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from ...permissions import CamomillaBasePermissions


class GetUserLanguageMixin(object):
    def _get_user_language(self):
        return self.request.GET.get(
            'language', self.request.data.get(
                'language_code', settings.LANGUAGE_CODE
            )
        )

    def get_queryset(self):
        user_language = self._get_user_language()
        fallbacks = True
        if len(user_language.split('-')) == 2 and user_language.split('-')[0] == 'nofallbacks':
            fallbacks = False
            user_language = user_language.split('-')[1]
        return self.model.objects.language(user_language).fallbacks().all() if fallbacks else self.model.objects.language(user_language).all()


class BulkDeleteMixin(object):
    @action(detail=False, methods=['post'], permission_classes=(CamomillaBasePermissions,))
    def bulk_delete(self, request):
        try:
            self.model.objects.filter(pk__in=request.data).delete()
            return Response({'detail': 'Eliminazione multipla andata a buon fine' }, status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'Eliminazione multipla non riuscita' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TrashMixin(object):
    @action(detail=False, methods=['post'], permission_classes=(CamomillaBasePermissions,))
    def bulk_trash(self, request):
        if request.data['action'] == 'restore':
            try:
                for element in self.model.objects.filter(pk__in=request.data['list']):
                    element.trash = False
                    element.save()
                return Response({'detail': 'Elementi correttamente rirpistinati' }, status=status.HTTP_200_OK)
            except:
                return Response({'detail': 'Non è stato possibile rirpistinare gli elementi' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        elif request.data['action'] == 'trash':
            try:
                for element in self.model.trashmanager.filter(pk__in=request.data['list']):
                    element.trash = True
                    element.save()
                return Response({'detail': 'Elementi correttamente spostati nel cestino' }, status=status.HTTP_200_OK)
            except:
                return Response({'detail': 'Non è stato possibile spostare gli elementi nel cestino' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'], permission_classes=(CamomillaBasePermissions,))
    def bulk_delete(self, request):
        try:
            self.model.trashmanager.trash(True).filter(pk__in=request.data).delete()
            return Response({'detail': 'Eliminazione multipla andata a buon fine' }, status=status.HTTP_200_OK)
        except:
            return Response({'detail': 'Eliminazione multipla non riuscita' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], permission_classes=(CamomillaBasePermissions,))
    def trash(self, request):
        self.serializer_class = self.get_serializer_class()
        serialized = self.serializer_class(self.model.trashmanager.trash(), many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], permission_classes=(CamomillaBasePermissions,))
    def not_in_trash(self, request):
        self.serializer_class = self.get_serializer_class()
        serialized = self.serializer_class(self.model.trashmanager.trash(False), many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
