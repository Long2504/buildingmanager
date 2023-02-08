from typing import Text
from django.db import models




# Create your models here.
class Floor(models.Model):
    name = models.TextField(max_length=255)
    capacity=models.IntegerField()
    status=models.TextField(max_length=255)
    area=models.IntegerField()
    deleted_flag=models.BooleanField(default=True)
    image=models.ImageField(upload_to='static/image/floor/',blank=True)
    
    def __str__(self):
        return f"{self.name,self.capacity,self.status,self.area,self.deleted_flag,self.image}"
