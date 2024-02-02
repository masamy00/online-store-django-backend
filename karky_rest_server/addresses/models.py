from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100, null=False, blank=False)
    is_master = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.city_name


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)
    street = models.CharField(max_length=255, null=False, blank=False)
    address_line1 = models.CharField(max_length=255, null=False, blank=False)
    address_line2 = models.CharField(max_length=255, null=False, blank=False)
    building = models.CharField(max_length=255, null=False, blank=False)
    floor = models.IntegerField(null=False, blank=False,
                                validators=[MinValueValidator(0, message="Value must be greater than or equal to 0.")])
