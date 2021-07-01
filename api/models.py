from django.db import models
from django.db.models.deletion import CASCADE


class product(models.Model):
    description = models.CharField(max_length=30, unique=True)
    user = models.CharField(max_length=30)
    dateUp = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.ForeignKey('api.categories', on_delete=CASCADE, unique=False)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    stock = models.IntegerField()
    image = models.CharField(max_length=500)
    active = models.BooleanField(default=True)

class categories(models.Model):
    description = models.CharField(max_length=35, unique=True)
    
class order(models.Model):
    status = models.ForeignKey('api.status', on_delete=CASCADE, unique=False, default=1)
    date_up = models.DateTimeField(auto_now_add=True, blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=25)
    user = models.CharField(max_length=30)
    dateInProcess = models.DateTimeField(blank=True, null=True)
    dateCompleted = models.DateTimeField(blank=True, null=True)
    dateDelivered = models.DateTimeField(blank=True, null=True)
    dateCanceled = models.DateTimeField(blank=True, null=True)

class status(models.Model):
    description = models.CharField(max_length=35, unique=True)
    

class order_details(models.Model):
    order = models.ForeignKey('api.order', on_delete=CASCADE, unique=False)
    codProd = models.IntegerField()
    quantity = models.IntegerField()
    priceProd = models.DecimalField(decimal_places=2, max_digits=5)
