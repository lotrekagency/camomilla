from django.core.management.base import BaseCommand
from ...utils import get_camomilla_model


class Command(BaseCommand):

    help = "Regenerates all the thumbnail"

    def handle(self, *args, **options):
        for media in get_camomilla_model("media").objects.all():
            media.regenerate_thumbnail()
            media.save()
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully regenerated thumbnail for {0}".format(media.file.url)
                )
            )
