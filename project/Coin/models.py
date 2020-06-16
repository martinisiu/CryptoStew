from django.db import models
import datetime
# Create your models here.

class BitcoinEntry(models.Model):
    price = models.CharField(max_length=20)
    utc = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Bitcoin Entry @ " + str(self.date)
    
    def getUTC(self):
        return self.utc