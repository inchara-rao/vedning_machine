from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class reset(models.Model):
    coke=models.CharField(max_length=5)
    pepsi = models.CharField(max_length=5)
    soda=models.CharField(max_length=5)
    penny_1= models.CharField(max_length=5)
    nickel_5 = models.CharField(max_length=5)
    dime_10 = models.CharField(max_length=5)
    quarter_25 = models.CharField(max_length=5)

class coins(models.Model):
    penny_1 = models.IntegerField(default=0)
    nickel_5 = models.IntegerField(default=0 )
    dime_10 = models.IntegerField( default=0)
    quarter_25 = models.IntegerField( default=0)
    Coke=models.IntegerField( default=0)
    Pepsi=models.IntegerField( default=0)
    Soda=models.IntegerField( default=0)
    Cancel=models.BooleanField(default=False)