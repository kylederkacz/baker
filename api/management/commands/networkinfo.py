import ifcfg

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        return self.execute(*args, **options)

    def execute(self, *args, **options):
        return ifcfg.interfaces()
