from ..mixins import OptimViewMixin, PaginateStackMixin, OrderingMixin
from rest_framework import viewsets


class BaseModelViewset(
    OptimViewMixin, OrderingMixin, PaginateStackMixin, viewsets.ModelViewSet
):
    pass
