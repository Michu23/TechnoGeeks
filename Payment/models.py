from django.db import models
from Student.models import Student
import datetime

# Create your models here.
class Payment(models.Model):

    STATUS = (
    ('Pending','Pending'),
    ('Completed','Completed'),
    ('Expired','Expired'),
    ('Partially','Partially'),
    )

    TYPES =(
    ('CautionDeposit','CautionDeposit'),
    ('Rent','Rent'),
    ('BatchShift','BatchShift'),
    ('Upfront','Upfront'),
    )

    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    amount = models.IntegerField(default=0)
    upi = models.IntegerField()
    cash = models.IntegerField()
    status = models.CharField(max_length=10,choices=STATUS)
    types = models.CharField(max_length=20,choices=TYPES)
    date = models.DateField(default=datetime.date.today)
    totalamt = models.IntegerField(default=0)

    def __str__(self):
        return self.student.user.username
