from .mixins import GetUserLanguageMixin, TrashMixin
from rest_framework.response import Response
from rest_framework import viewsets

from ..models import Article
from ..serializers import ExpandedArticleSerializer, ArticleSerializer
from ..permissions import CamomillaBasePermissions


class ArticleViewSet(GetUserLanguageMixin, TrashMixin, viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (CamomillaBasePermissions,)
    model = Article
    serializers = {
        "compressed": ArticleSerializer,
        "expanded": ExpandedArticleSerializer,
    }

    def get_dynamic_serializer(self, request):
        compressed = request.GET.get("compressed", False)
        current_serializer = self.serializers["expanded"]
        if compressed:
            current_serializer = self.serializers["compressed"]
        return current_serializer

    def list(self, request, *args, **kwargs):
        user_language = self._get_user_language()

        # Filter by status
        status = request.GET.get("status", None)
        # Filter by page
        page = request.GET.get("page", None)
        queryset = self.get_queryset()
        if status:
            queryset = queryset.filter(status=status)

        # Support pagination
        current_serializer = self.get_dynamic_serializer(request)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = current_serializer(
                page, many=True, ulanguage=user_language, context={"request": request}
            )
            return self.get_paginated_response(serializer.data)

        # Serialize
        serializer = current_serializer(
            queryset, many=True, ulanguage=user_language, context={"request": request}
        )
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        user_language = self._get_user_language()
        current_serializer = self.get_dynamic_serializer(request)
        instance = self.get_queryset().get(pk=kwargs["pk"])
        serializer = current_serializer(
            instance, ulanguage=user_language, context={"request": request}
        )
        return Response(serializer.data)
