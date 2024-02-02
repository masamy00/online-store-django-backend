from django.db import models
from addresses.models import Address


# Create your models here.
class Merchant(models.Model):
    merchant_id = models.AutoField(primary_key=True)
    merchant_en_name = models.CharField(max_length=255, null=False, blank=False)
    merchant_ar_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.merchant_en_name


class MerchantAddress(models.Model):
    merchant_address_id = models.AutoField(primary_key=True)
    merchant_id = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)

