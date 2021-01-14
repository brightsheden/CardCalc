from django.db import models

# Create your models here.
class AirtimesMtn(models.Model):
    Title = models.CharField(max_length=200)  
    Mtn_500 = models.CharField(max_length=200)
    Mtn_200 = models.CharField(max_length=200)
    Mtn_100 = models.CharField(max_length=200)

class AirtimesGlo(models.Model):
    Title = models.CharField(max_length=200)
    Glo_500 = models.CharField(max_length=200)
    Glo_200 = models.CharField(max_length=200)
    Glo_100 = models.CharField(max_length=200)

class AirtimesAirtel(models.Model):
    Title = models.CharField(max_length=200)
    Airtel_500 = models.CharField(max_length=200)
    Airtel_200 = models.CharField(max_length=200)
    Airtel_100 = models.CharField(max_length=200)   