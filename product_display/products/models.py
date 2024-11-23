from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    discounted_price = models.CharField(max_length=50)
    actual_price = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()
    product_url = models.URLField()

    def __str__(self):
        return self.name
