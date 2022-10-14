import random
from django.core.management.base import BaseCommand
from faker import Faker
from orders.models import Orders


class Command(BaseCommand):
    help = 'Command information'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(1000):
            Orders.objects.create(
                product_id=random.randint(1, 1000),
                quantity=random.randint(1, 250),
                total_price=(round(random.uniform(0.01, 99999999.99), 2)),
                invoice_date=fake.date_time()
            )
