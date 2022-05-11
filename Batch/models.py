from django.db import models
from Admin.models import Advisor
from User.models import Domain

# Create your models here.

#Batch
class Batch(models.Model):
    batchno = models.IntegerField()
    advisor = models.ForeignKey(Advisor,on_delete=models.SET_NULL,null=True)

class Group(models.Model):
    name = models.CharField(max_length=5)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL,null=True)
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL,null=True)
    advisor = models.ForeignKey(Advisor,on_delete=models.SET_NULL,null=True)