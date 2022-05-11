from django.db import models
from Student.models import Student

# Create your models here.
class Payment(models.Model):

    STATUS = (
    ('Pending','Pending'),
    ('Completed','Completed'),
    ('Expired','Expired')
    )

    TYPES =(
    ('CautionDeposit','CautionDeposit'),
    ('Rent','Rent'),
    ('BatchShift','BatchShift'),
    ('Upfront','Upfront'),
    )

    student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True)
    amount = models.IntegerField()
    UPI = models.IntegerField()
    cash = models.IntegerField()
    status = models.CharField(max_length=10,choices=STATUS)
    types = models.CharField(max_length=20,choices=TYPES)
