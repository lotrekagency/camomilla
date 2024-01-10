from collections import defaultdict
from typing import Callable, Optional, TYPE_CHECKING, Type, Dict
import inspect
from django.http import HttpRequest

if TYPE_CHECKING:
    from camomilla.models.page import AbstractPage


class PagesContextRegistry:
    def __init__(self) -> None:
        self._model_registry = defaultdict(set)
        self._template_registry = defaultdict(set)

    def register(
        self,
        func: Callable,
        template_path: Optional[str],
        page_model: Optional[Type["AbstractPage"]],
    ):
        assert (
            template_path is not None or page_model is not None
        ), "You must provide at least one between template_path and page_model"
        if template_path is not None:
            self._template_registry[template_path].add(func)
        if page_model is not None:
            self._model_registry[page_model].add(func)

    def get_registered_info(self) -> Dict[str, dict]:
        info = defaultdict(dict)
        for k, v in self._template_registry.items():
            for f in v:
                key = f"{f.__module__}.{f.__name__}"
                info[key]["templates"] = info[key].get("templates", set())
                info[key]["templates"].add(k)
                info[key]["templates_count"] = len(info[key]["templates"])
        for k, v in self._model_registry.items():
            key = f"{f.__module__}.{f.__name__}"
            for f in v:
                info[key]["models"] = info[key].get("models", set())
                info[key]["models"].add(k)
                info[key]["models_count"] = len(info[key]["models"])
        return info

    def get_wrapper_context_func(
        self, template_path: str, page_model: Type["AbstractPage"]
    ) -> Callable:
        all_funcs = set()
        for cls in self._model_registry.keys():
            if issubclass(page_model, cls):
                all_funcs.update(self._model_registry[cls])
        all_funcs.update(self._template_registry[template_path])

        def context_func(request: HttpRequest, super_ctx: dict = {}):
            context = super_ctx.copy()
            for func in all_funcs:
                arg_spec = inspect.getfullargspec(func)
                kwargs = {}
                if "request" in arg_spec.args:
                    kwargs["request"] = request
                if "super_ctx" in arg_spec.args:
                    kwargs["super_ctx"] = context
                context.update(func(**kwargs) or {})
            return context

        return context_func

    def get_context_for_page(self, page: "AbstractPage", request, super_ctx: dict = {}):
        return self.get_wrapper_context_func(
            page.get_template_path(request), page.__class__
        )(request, super_ctx=super_ctx)


def register(
    template_path: Optional[str] = None,
    page_model: Optional[Type["AbstractPage"]] = None,
):
    assert (
        template_path is not None or page_model is not None
    ), "You must provide at least one between template_path and page_model"

    def inner(func: Callable):
        ctx_registry.register(func, template_path, page_model)
        return func

    return inner


ctx_registry = PagesContextRegistry()
