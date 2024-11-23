import csv
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = "Load products from a CSV file"

    def handle(self, *args, **kwargs):
        with open('products/amazon.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Product.objects.create(
                    name=row['product_name'],
                    discounted_price=row['discounted_price'],
                    actual_price=row['actual_price'],
                    description=row['about_product'],
                    image_url=row['img_link'],
                    product_url=row['product_link']
                )
        self.stdout.write(self.style.SUCCESS("Products loaded successfully!"))
