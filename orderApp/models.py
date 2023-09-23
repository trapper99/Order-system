import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=200, decimal_places=2)
    weight = models.DecimalField(max_digits=200, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    
class Shipment(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    )
    
    id_reference = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    owner_name = models.CharField(max_length=250)
    owner_email = models.CharField(max_length=250)
    shipment_date = models.DateTimeField(default=timezone.now)
    status_info = models.CharField(max_length=200, choices=STATUS, default='Pending')    