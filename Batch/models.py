from django.db import models
from Admin.models import Advisor
from User.models import Domain

# Create your models here.

#Batch
class Batch(models.Model):
    code = models.CharField(max_length=20, unique=True, null=True)
    batchno = models.IntegerField()
    location = models.CharField(max_length=30, null=True, blank=True)
    advisor = models.ForeignKey(Advisor,on_delete=models.SET_NULL,null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        name = str(self.batchno) + ' ' + str(self.id)
        return name

class Group(models.Model):
    name = models.CharField(max_length=10)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL,null=True)
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL,null=True)
    advisor = models.ForeignKey(Advisor,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name