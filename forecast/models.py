from django.db import models

class Charges(models.Model):
    region = models.CharField(unique=True, max_length=128)
    amount_per_month = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.region)

class Balance(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField()