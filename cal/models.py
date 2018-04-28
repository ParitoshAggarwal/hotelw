from django.db import models

# Create your models here.


class hotelcal(models.Model):
    month = models.CharField(max_length=10)
    date = models.IntegerField()
    single = models.IntegerField()
    double = models.IntegerField()
    single_price = models.FloatField()
    double_price = models.FloatField()
    day = models.CharField(max_length=10)

    def __str__(self):
        return self.month+str(self.date)