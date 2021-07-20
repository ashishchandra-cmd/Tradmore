from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Currencies(models.Model):
    currencies = models.CharField(max_length=12 ,unique=True)



class TradingData(models.Model):
    currency  = models.ForeignKey(Currencies,on_delete=models.CASCADE)
    price = models.FloatField()
    open_price = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    change_percentage = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return self.currency

class UserHistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.FloatField()
    action = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)

class NotifyData(models.Model):
    msg = models.CharField(max_length=500)
    send_to_all = models.BooleanField(default=False)

