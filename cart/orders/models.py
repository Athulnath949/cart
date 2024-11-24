from django.db import models
from customers.models import customer
from products.models import product
class order(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))

    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,delete)
    create_at=models.DateTimeField(auto_now_add=true)
    updated_at=models.DataTimeField(auto_now=true)


class orderItem(models.Model):
    product=models.ForeignKey(product,related_name='added_carts',on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=1)
    
