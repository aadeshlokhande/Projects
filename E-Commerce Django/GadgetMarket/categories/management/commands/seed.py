from faker import Faker
from  django.core.management.base import BaseCommand
from django.utils import timezone
from django.apps import  apps
from django.contrib.auth import get_user_model

fake = Faker()

class Command(BaseCommand):
    help = 'generate fake categories'
    def handle(self, *args, **kwargs):
        User = get_user_model()
        categories = apps.get_model("categories","Categories")
        number_of_record = 100
        for _ in range(number_of_record):
            name = fake.unique.word()
            description = fake.sentence()
            created_by = User.objects.get(id=2)
            updated_by = User.objects.get(id=2)
            updated_at = timezone.now()

            categories.objects.create(name=name,description=description,created_by=created_by,updated_by=updated_by,updated_at=updated_at)
        self.stdout.write(self.style.SUCCESS(f'successfully generated {number_of_record} fake categories'))