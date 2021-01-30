from rest_framework import viewsets
from rest_framework.response import Response
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.postgres.search import SearchVector, SearchQuery


class BaseModelViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super(BaseModelViewSet, self).get_serializer_class()

    def get_serializer_context(self):
        return {"request": self.request, "action": self.action}

    def get_queryset(self):
        queryset = super(BaseModelViewSet, self).get_queryset()
        serializer = self.get_serializer_class()
        if hasattr(serializer, "setup_eager_loading"):
            queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class PaginateStackMixin(BaseModelViewSet):
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
        items_per_page = items_per_page or getattr(self, "items_per_page", 30)
        paginator = Paginator(list_handler, items_per_page)
        page = self.request.GET.get("page")

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
        sort = self.request.GET.get("sort", None)
        order = self.request.GET.get("order", "asc")
        if sort:
            return list_handler.order_by(f"{'-' if order == 'desc' else ''}{sort}")
        elif order == "desc":
            return list_handler.reverse()
        return list_handler

    def handle_filters(self, list_handler=None):
        list_handler = list_handler if list_handler is not None else self.get_queryset()
        filters = dict(self.request.GET).get("fltr", [])
        for filter in filters:
            try:
                filter_name, value = self.parse_filter(filter)
                list_handler = list_handler.filter(**{filter_name: value})
            except:
                pass
        return list_handler

    def handle_search(self, list_handler=None, search_fields=None):
        list_handler = list_handler if list_handler is not None else self.get_queryset()
        search_string = self.request.GET.get("search", None)
        if search_string:
            return list_handler.annotate(
                search=SearchVector(
                    search_fields or getattr(self, "search_fields", [])
                ),
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
                "page_range": list(paginator.page_range),
                "page_size": paginator.per_page,
            },
        }

    def list(self, *args, **kwargs):
        return Response(
            self.format_output(*self.handle_pagination_stack(self.get_queryset()))
        )
