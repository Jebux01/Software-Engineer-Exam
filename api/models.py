from django.db import models
from django.db.models.deletion import CASCADE

class product(models.Model):
    codeProd = models.OneToOneField('api.product', on_delete=CASCADE, editable=False, primary_key=True, unique=True)
    description = models.CharField(max_length=30)
    user = models.CharField(max_length=30)
    dateUp = models.DateTimeField()
    category = models.OneToOneField('api.categories', on_delete=CASCADE, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    stock = models.IntegerField()
    image = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

class categories(models.Model):
    description = models.CharField(max_length=35)
    
class order(models.Model):
    id_order = models.OneToOneField('api.order', on_delete=CASCADE, editable=False, primary_key=True, unique=True)
    status = models.IntegerField()
    date_up = models.DateTimeField()
    subtotal = models.DecimalField(decimal_places=2, max_digits=5)
    total = models.DecimalField(decimal_places=2, max_digits=5)
    user = models.CharField(max_length=30)
    dateInProcess = models.DateTimeField(blank=True)
    dateCompleted = models.DateTimeField(blank=True)
    dateDelivered = models.DateTimeField(blank=True)
    dateCanceled = models.DateTimeField(blank=True)
    

class order_details(models.Model):
    id_order = models.IntegerField(editable=False)
    codProd = models.IntegerField()
    quantity = models.IntegerField()
    priceProd = models.DecimalField(decimal_places=2, max_digits=5)
