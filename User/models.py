from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Department(models.Model):
    DEPARTMENT = (
    ('Student','Student'),
    ('Advisor','Advisor'),
    ('Accounts','Accounts'),
    ('Lead','Lead')
    )

    name = models.CharField(max_length=20, choices = DEPARTMENT)

    def __str__(self):
        return self.name

class User(AbstractUser):
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    is_lead = models.BooleanField(default=False,null=True)
    is_student = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.username

class Domain(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Profile(models.Model):

    GENDER = (
    ('Male','Male'),
    ('Female','Female')
    )

    first_name = models.CharField(max_length=20,null=True, blank=True, default='')
    last_name = models.CharField(max_length=20,null=True, blank=True, default='')
    photo = models.ImageField(upload_to='Media/Profile',blank=True, default='Media/Profile/defaultProPic.png')
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL,null=True, blank=True)
    dob= models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length = 7,choices = GENDER, default = '')
    address = models.TextField(null=True, blank=True,max_length=100, default='')
    village = models.CharField(max_length=20,null=True, blank=True, default='')
    education = models.CharField(max_length=20,null=True, blank=True, default='')
    college = models.CharField(max_length=20,null=True, blank=True, default='')
    experience = models.CharField(max_length=20,null=True, blank=True, default='')
    company = models.CharField(max_length=20,null=True, blank=True, default='')
    designation = models.CharField(max_length=20,null=True, blank=True, default='')
    mobile = models.IntegerField(null=True, blank=True, default=0)
    govtid = models.ImageField(upload_to='Media/Id',blank=True)

    def __str__(self):
        try:
            return self.advisor.user.username
        except:
            return self.student.user.username
