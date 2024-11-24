from django.db import models

class product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'delete'))
    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='/media')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,delete)
    create_at=models.DateTimeField(auto_now_add=true)
    updated_at=models.DataTimeField(auto_now=true)
    

    def __str__(self) -> str:
        return self.title