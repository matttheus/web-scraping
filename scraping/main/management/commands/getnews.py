from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "This commands get news from the web"

    def handle(self, *args, **kwargs):
        try:
            print('command created')
        except:
            raise CommandError("Somethings went wrong")