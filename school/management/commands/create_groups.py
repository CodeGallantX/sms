from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Creates the default groups'

    def handle(self, *args, **options):
        groups = ['Student', 'Teacher', 'Admin']
        for group in groups:
            if not Group.objects.filter(name=group).exists():
                Group.objects.create(name=group)
                self.stdout.write(self.style.SUCCESS(f'Successfully created {group} group'))
            else:
                self.stdout.write(self.style.WARNING(f'{group} group already exists'))
