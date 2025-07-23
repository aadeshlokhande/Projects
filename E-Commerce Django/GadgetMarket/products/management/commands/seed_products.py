from faker import Faker
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.apps import apps
from django.contrib.auth import get_user_model
from categories.models import Categories

fake = Faker()

# name ===========
# description ===========
# category ==========
# image ---- None
# price =============
# quantity ==========
# status = 1 -----
# is delete = 0 -----
# created at ---> current -------
# updated at ----> current ============
# created by ----> admin ===========
# updated by -----> admin ==========

class Command(BaseCommand):
    help = 'generate fake products'
    def handle(self, *args, **kwargs):
        User = get_user_model()
        products = apps.get_model("products","Products")
        # categories = apps.get_model("categories","Categories")
        number_of_record = 50000
        for _ in range(number_of_record):
            cat_id=""
            try:
                cat_id = fake.random_number(digits=2)
                category_obj = Categories.objects.get(id=cat_id)
                if category_obj is None:
                    cat_id = 98
                    category_obj = Categories.objects.get(id=cat_id)
                name = fake.word()
                description = fake.sentence()
                category = category_obj
                quantity = fake.random_number(digits=2)
                price = fake.random_number(digits=5)
                created_by = User.objects.get(id=2)
                updated_by = User.objects.get(id=2)
                updated_at = timezone.now()

                products.objects.create(name=name,description=description,category=category,quantity=quantity,price=price,created_by=created_by,updated_by=updated_by,updated_at=updated_at)
            except Exception as e:
                print("category_id:",cat_id)
                print(e)
        self.stdout.write(self.style.SUCCESS(f'successfully generated {number_of_record} fake categories'))