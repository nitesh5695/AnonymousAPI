# Create your models here.
from django.db import models
class anonymousUser(models.Model):
    username=models.CharField(max_length=100,unique=True)
    def is_authenticated():
        return True
    def __str__(self):
        return self.username

class customer_model(models.Model):
 name = models.CharField(max_length=50)
 mobile = models.IntegerField()
 customer_type = models.CharField(max_length=50)
   
