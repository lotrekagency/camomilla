from django.db import models
from hvad.models import TranslatableModel, TranslatedFields

from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language

from .utils import get_complete_url
from .manager import TranslationTrashManager, TrashManager

class SeoMixin(TranslatableModel):

    seo_attr = 'identifier'

    translations = TranslatedFields(
        title = models.CharField(max_length=200),
        description = models.TextField(blank=True, null=True, default=''),
        permalink = models.CharField(max_length=200, blank=True),
        og_description = models.TextField(blank=True, null=True, default=''),
        og_title = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_type = models.CharField(max_length=200, blank=True, null=True, default=''),
        og_url = models.CharField(max_length=200, blank=True, null=True, default=''),
        canonical = models.CharField(max_length=200, blank=True, null=True, default=''),
    )
    og_image = models.ForeignKey('camomilla.Media', blank=True, null=True, on_delete=models.SET_NULL, related_name="%(app_label)s_%(class)s_related")

    @classmethod
    def with_seo(model, request, identifier, lang=''):
        if not lang:
            lang = get_language()
        try:
            kwargs = {model.seo_attr: identifier}
            meta_tag, _ = model.objects.language().get_or_create(**kwargs)
            if not meta_tag.og_title:
                meta_tag.og_title = meta_tag.title
            if not meta_tag.og_description:
                meta_tag.og_description = meta_tag.description
            permalink = request.path
            if not meta_tag.permalink:
                meta_tag.permalink = permalink
            if not meta_tag.canonical:
                meta_tag.canonical = get_complete_url(request, permalink, lang)
            else:
                meta_tag.canonical = get_complete_url(request, meta_tag.canonical, lang)
            if not meta_tag.og_url:
                meta_tag.og_url = meta_tag.canonical
            else:
                meta_tag.og_url = get_complete_url(request, meta_tag.og_url,lang)
            return meta_tag

        except model.DoesNotExist:
            return None

    class Meta:
        abstract = True


class SlugMixin(object):

    slug_attr = 'title'

    def get_slug(self):
        return self.slug

    get_slug.short_description = _('Slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(getattr(self, self.slug_attr))
        super(SlugMixin, self).save(*args, **kwargs)


class TrashMixin(object):
    trash = models.BooleanField(default=False)
    trashmanager = TrashManager()
    
    class Meta:
        abstract = True


class TranslationTrashMixin(TranslatableModel):
    trash = models.BooleanField(default=False)
    trashmanager = TranslationTrashManager()
    translations = TranslatedFields()
    
    class Meta:
        abstract = True
