from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Department(models.Model):
    DEPARTMENT = (
    ('Advisor','Advisor'),
    ('Communication','Communication'),
    ('Finance','Finance'),
    ('Lead','Lead'),
    ('Placement','Placement'),
    ('Student','Student'),
    )

    name = models.CharField(max_length=20, choices = DEPARTMENT)

    def __str__(self):
        return self.name

class User(AbstractUser):
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    is_lead = models.BooleanField(default=False,null=True)
    is_student = models.BooleanField(default=False,null=True)

    def __str__(self):
        s = self.username + " " + str(self.id)
        return s

class Domain(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        s = self.name + " " + str(self.id)
        return s

class Profile(models.Model):

    GENDER = (
    ('Male','Male'),
    ('Female','Female')
    )

    first_name = models.CharField(max_length=20,null=True, blank=True, default='')
    last_name = models.CharField(max_length=20,null=True, blank=True, default='')
    photo = models.ImageField(upload_to='Media/Profile',blank=True, default='Media/Profile/defaultProPic.png')
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL,null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length = 7,choices = GENDER, default = '')
    father = models.CharField(max_length=20,null=True, blank=True, default='')
    father_contact = models.BigIntegerField(null=True, blank=True, default=None)
    mother = models.CharField(max_length=20,null=True, blank=True, default='')
    mother_contact = models.BigIntegerField(null=True, blank=True, default=None)
    guardian = models.CharField(max_length=20,null=True, blank=True, default='')
    relation = models.CharField(max_length=20,null=True, blank=True, default='')
    address = models.TextField(null=True, blank=True,max_length=100, default='')
    village = models.CharField(max_length=20,null=True, blank=True, default='')
    taluk = models.CharField(max_length=20,null=True, blank=True, default='')
    education = models.CharField(max_length=20,null=True, blank=True, default='')
    college = models.CharField(max_length=20,null=True, blank=True, default='')
    experience = models.CharField(max_length=20,null=True, blank=True, default='')
    company = models.CharField(max_length=20,null=True, blank=True, default='')
    designation = models.CharField(max_length=20,null=True, blank=True, default='')
    mobile = models.BigIntegerField(null=True, blank=True, default=None)
    govtid = models.ImageField(upload_to='Media/Id',blank=True)

    def __str__(self):
        try:
            return self.advisor.user.username
        except:
            return self.student.user.username

class Notification(models.Model):
    TYPE = (
    ('Placement','Placement'),
    ('AdvisorChange','Advisor Change'),
    ('BatchShift','Batch Shift'),
    ('Termination','Termination'),
    )

    type = models.CharField(max_length=20, choices=TYPE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type