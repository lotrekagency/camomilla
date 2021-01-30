from hvad.manager import TranslationManager, TranslationQueryset
from django.db import models


class TranslationTrashQueryset(TranslationQueryset):
    def trash(self, bin=False):
        return self.exclude(trash=False) if bin else self.exclude(trash=True)


class TranslationTrashManager(TranslationManager):

    queryset_class = TranslationTrashQueryset
    default_class = TranslationTrashQueryset
    fallback_class = TranslationTrashQueryset

    def trash(self, bin=False):
        return super(TranslationTrashManager, self).get_queryset().trash(bin)


class TrashManager(models.Manager):
    def get_queryset(self):
        return super(TrashManager, self).get_queryset().exclude(trash=True)

    def trash(self):
        return super(TrashManager, self).get_queryset().exclude(trash=False)
