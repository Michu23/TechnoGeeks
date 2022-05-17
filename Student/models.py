from django.db import models
from Batch.models import Batch, Group
from User.models import User, Profile

# Create your models here.


class Student(models.Model):

    STATUS=(
    ('Training','Training'),
    ('Placed','Placed'),
    ('RequestedTermination','RequestedTermination'),
    ('Terminated','Terminated')
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    batch= models.ForeignKey(Batch, on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=20,choices=STATUS)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,null=True)
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)

class Placement(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    position = models.CharField(max_length=20,null=True, blank=True)
    company = models.CharField(max_length=30,null=True, blank=True)
    location = models.CharField(max_length=20,null=True, blank=True)
    LPA= models.FloatField()

class Shifted(models.Model):
    student= models.ForeignKey(Student, on_delete=models.SET_NULL,null=True)
    shifted_to = models.ForeignKey(Batch, on_delete=models.SET_NULL,null=True,blank=True)
    shifted_in = models.ForeignKey(Batch, on_delete=models.SET_NULL,null=True,blank=True,related_name="come_from")
    date= models.DateTimeField(auto_now_add=True)


