from django.core.management.base import BaseCommand, CommandError
from camomilla.models import Media


class Command(BaseCommand):

    help = 'Optimize all the images'

    def handle(self, *args, **options):
        for media in Media.objects.all():
            self.stdout.write(self.style.ERROR(
                '===================='
            ))
            self.stdout.write(self.style.SUCCESS(
                'Optimize image {0}'.format(media.file.url)
            ))
            media.optimize()
            self.stdout.write(self.style.ERROR(
                '===================='
            ))
