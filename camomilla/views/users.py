from .base import BaseModelViewset
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from django.db.models import Q

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action

from ..serializers import (
    UserProfileSerializer,
    UserSerializer,
    PermissionSerializer,
)
from ..permissions import CamomillaSuperUser


class CamomillaObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class UserViewSet(BaseModelViewset):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    model = get_user_model()
    permission_classes = (CamomillaSuperUser,)

    @action(
        detail=False,
    )
    def current(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def kickout(self, request, pk=None):
        user = get_user_model().objects.get(pk=pk)
        try:
            user.auth_token.delete()
        except Exception:
            pass

        return Response({})


class PermissionViewSet(BaseModelViewset):

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    model = Permission
    permission_classes = (CamomillaSuperUser,)
    http_method_names = ["get", "put", "options", "head"]

    def get_queryset(self):
        permissions = Permission.objects.filter(
            Q(content_type__app_label__contains="camomilla")
            | Q(content_type__app_label__contains="plugin_")
            | Q(content_type__model="token")
            | Q(content_type__model="user")
        )
        return permissions


class UserProfileViewSet(BaseModelViewset):

    queryset = get_user_model().objects.all()
    serializer_class = UserProfileSerializer
    model = get_user_model()
    http_method_names = ["get", "put", "options", "head"]

    @action(detail=False, methods=["get"])
    def me(self, request):
        personal_profile = request.user
        return Response(
            self.serializer_class(personal_profile, context={"request": request}).data
        )
