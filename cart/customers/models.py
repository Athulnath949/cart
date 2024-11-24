from django.db import models

class customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    name=models.CharField(max_length=200)
    address=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')
    phone=models.CharField(max_length=10)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,delete)
    create_at=models.DateTimeField(auto_now_add=true)
    updated_at=models.DataTimeField(auto_now=true)
    

    def __str__(self) -> str:
        return self.name
