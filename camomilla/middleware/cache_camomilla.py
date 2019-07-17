from django.middleware.cache import FetchFromCacheMiddleware


class CacheCamomillaMiddleware(FetchFromCacheMiddleware):
    def process_request(self, request):
        print ('middleware')
        if request.META.get('HTTP_DISABLE_CACHE', ''):
            request._cache_update_cache = False
            return None
        if request.user and request.user.is_authenticated and request.user.is_superuser:
            print ('cache super')
            request._cache_update_cache = False
            return None
        return super(CacheCamomillaMiddleware, self).process_request(request)
