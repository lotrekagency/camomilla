from django.contrib.sitemaps import Sitemap
from camomilla.models import UrlNode


class CamomillaPagesSitemap(Sitemap):
    changefreq_default = "daily"
    priority_default = 0.5

    def changefreq(self, obj):
        if hasattr(obj.page.__class__, "changefreq"):
            return obj.page.changefreq
        return self.changefreq_default

    def priority(self, obj):
        if hasattr(obj.page.__class__, "priority"):
            return obj.priority
        return self.priority_default

    def items(self):
        return UrlNode.objects.filter(is_public=True)

    def lastmod(self, obj):
        if hasattr(obj.page.__class__, "lastmod"):
            return obj.page.lastmod
        return obj.date_updated_at


camomilla_sitemaps = {
    "pages": CamomillaPagesSitemap,
}
