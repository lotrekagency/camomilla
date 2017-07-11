from django.middleware.cache import FetchFromCacheMiddleware


class CacheCamomillaMiddleware(FetchFromCacheMiddleware):
    def process_request(self, request):
        if request.META.get('HTTP_DISABLE_CACHE', ''):
            return None
        if request.user and request.user.is_superuser:
            return None
        if request.user and request.user.is_authenticated():
            if request.user.level == '3' or request.user.level == '2':
                return None
        return super(CacheCamomillaMiddleware, self).process_request(request)
