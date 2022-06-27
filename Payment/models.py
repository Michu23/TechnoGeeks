from django.db import models
from Student.models import Student
import datetime
from datetime import timedelta


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
    ('Fine','Fine'),
    )
    
    MONTH = (
        ('---','---'),
        ('January','January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December'),
    )

    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    amount = models.IntegerField(default=0,null=True,blank=True)
    paid = models.IntegerField(default=0,null=True,blank=True)
    upi = models.IntegerField(null=True,blank=True,default=0)
    cash = models.IntegerField(null=True,blank=True,default=0)
    status = models.CharField(max_length=10,choices=STATUS)
    types = models.CharField(max_length=20,choices=TYPES)
    date = models.DateField(default=datetime.date.today)
    totalamt = models.IntegerField(default=0,null=True,blank=True)
    month = models.CharField(max_length=20,choices=MONTH,default='---')
    paid_date = models.DateField(null=True,blank=True)
    expiry_date = models.DateField(null=True,blank=True,default=datetime.datetime.today()-datetime.timedelta(1))
    paymentid = models.CharField(max_length=25,null=True,blank=True)

    def __str__(self):
        name = self.student.user.username + " " + self.types + " " + self.status
        return name
