from django.core.management.base import BaseCommand, CommandError
from camomilla.models import Media


class Command(BaseCommand):

    help = 'Regenerates all the thumbnail'

    def handle(self, *args, **options):
        for media in Media.objects.all():
            if media.is_image:
                media.regenerate_thumbnail()
                self.stdout.write(self.style.SUCCESS(
                    'Successfully regenerated thumbnail for {0}'.format(media.file.url)
                ))
