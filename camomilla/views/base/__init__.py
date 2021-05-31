from ..mixins import OptimViewMixin, PaginateStackMixin
from rest_framework import viewsets


class BaseModelViewset(OptimViewMixin, PaginateStackMixin, viewsets.ModelViewSet):
    pass
