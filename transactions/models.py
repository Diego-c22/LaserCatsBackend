from django.db import models

# Create your models here.

class Sale(models.Model):
    wallet_to = models.CharField(max_length=200)
    timestamp = models.PositiveBigIntegerField(default=0)
    transaction_id = models.CharField(max_length=200)
    price_sale = models.DecimalField(max_digits=24, decimal_places=18)
    quantity = models.PositiveSmallIntegerField(default=1)