from django.db import models


class BaseTag(models.Model):
    title=models.CharField(max_length=200, unique=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Tag(BaseTag):
    pass