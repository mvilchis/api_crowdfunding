from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Help command message"

    def handle(self, **options):
        print 'hola'
