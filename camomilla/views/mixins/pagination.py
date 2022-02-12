from rest_framework.response import Response
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.postgres.search import SearchVector, SearchQuery, TrigramSimilarity


class TrigramSearchMixin:
    def handle_search(self, list_handler=None, search_fields=None):
        list_handler = list_handler if list_handler is not None else self.get_queryset()
        search_string = self.request.GET.get("search", None)
        search_fields = search_fields or getattr(self, "search_fields", [])
        if search_string and len(search_fields) > 0:
            filters = Q()
            for field in search_fields:
                filters |= Q(
                    **{f"search_{field}__gte": getattr(self, "trigram_threshold", 0.3)}
                )
            return list_handler.annotate(
                **{
                    f"search_{field}": TrigramSimilarity(field, search_string)
                    for field in search_fields
                },
            ).filter(filters)

        return list_handler


class PaginateStackMixin:
    def parse_qs_value(self, string: str):
        if string and string.startswith("[") and string.endswith("]"):
            string = [self.parse_qs_value(substr) for substr in string[1:-1].split(",")]
        elif string and string.lower() in ["true", "false"]:
            string = string.lower() == "true"
        elif string and string.isdigit():
            string = int(string)
        return string

    def parse_filter(self, filter):
        filter_name, value = filter.split("=")
        return filter_name, self.parse_qs_value(value)

    def handle_pagination(self, list_handler=None, items_per_page=None):
        list_handler = list_handler if list_handler is not None else self.get_queryset()
        items_per_page = int(
            items_per_page
            or self.request.GET.get("items")
            or getattr(self, "items_per_page", 30)
        )
        paginator = Paginator(
            list_handler,
            items_per_page if items_per_page != -1 else list_handler.count(),
        )
        page = self.request.GET.get("page", 1) if items_per_page != -1 else 1

        try:
            elements = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            elements = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            elements = paginator.page(paginator.num_pages)

        return paginator, elements

    def handle_ordering(self, list_handler=None):
        list_handler = list_handler if list_handler is not None else self.get_queryset()
        sort = [p for p in self.request.GET.get("sort", "").split(",") if p]
        order = self.request.GET.get("order", "asc")
        if sort:
            list_handler.order_by(*sort)
        if order == "desc":
            list_handler.reverse()
        return list_handler

    def handle_filters(self, list_handler=None):
        list_handler = list_handler if list_handler is not None else self.get_queryset()
        filters = dict(self.request.GET).get("fltr", [])
        for filter in filters:
            try:
                filter_name, value = self.parse_filter(filter)
                list_handler = list_handler.filter(**{filter_name: value})
            except Exception:
                pass
        return list_handler

    def handle_search(self, list_handler=None, search_fields=None):
        list_handler = list_handler if list_handler is not None else self.get_queryset()
        search_string = self.request.GET.get("search", None)
        search_fields = search_fields or getattr(self, "search_fields", [])
        if search_string and len(search_fields) > 0:
            return list_handler.annotate(
                search=SearchVector(*search_fields),
            ).filter(search=SearchQuery(search_string))

        return list_handler

    def handle_pagination_stack(
        self, list_handler=None, search_fields=None, items_per_page=None
    ):
        return self.handle_pagination(
            self.handle_ordering(
                self.handle_filters(self.handle_search(list_handler, search_fields))
            ),
            items_per_page,
        )

    def format_output(self, paginator, elements, SerializerClass=None):
        SerializerClass = SerializerClass or self.get_serializer_class()
        return {
            "items": SerializerClass(
                elements, many=True, context=self.get_serializer_context()
            ).data,
            "paginator": {
                "count": paginator.count,
                "page": elements.number,
                "has_next": elements.has_next(),
                "has_previous": elements.has_previous(),
                "pages": paginator.num_pages,
                "page_size": paginator.per_page,
            },
        }

    def list(self, *args, **kwargs):
        active = getattr(self, "force_active", False) or (
            self.request.GET.get("items", -1) != -1
        )
        return (
            Response(
                self.format_output(*self.handle_pagination_stack(self.get_queryset()))
            )
            if active
            else super().list(*args, **kwargs)
        )
