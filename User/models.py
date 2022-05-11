from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User(User):
    is_lead = models.BooleanField(default=False)

class Domain(models.Model):
    name = models.CharField(max_length=20)

class Profile(models.Model):

    GENDER = (
    ('---','---'),
    ('Male','Male'),
    ('Female','Female')
    )

    first_name = models.CharField(max_length=20,null=True, blank=True)
    last_name = models.CharField(max_length=20,null=True, blank=True)
    photo = models.ImageField(upload_to='images/profile',blank=True)
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL,null=True, blank=True)
    dob= models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length = 7,choices = GENDER, default = '---')
    address = models.TextField(null=True, blank=True,max_length=100)
    village = models.CharField(max_length=20,null=True, blank=True)
    education = models.CharField(max_length=20,null=True, blank=True)
    college = models.CharField(max_length=20,null=True, blank=True)
    experience = models.CharField(max_length=20,null=True, blank=True)
    company = models.CharField(max_length=20,null=True, blank=True)
    designation = models.CharField(max_length=20,null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    govtid = models.ImageField(upload_to='images',blank=True)
    userid=models.OneToOneField(User,on_delete=models.CASCADE)
