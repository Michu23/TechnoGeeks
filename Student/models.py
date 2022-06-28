from django.db import models
from Batch.models import Batch, Group, Branch
from User.models import User, Profile, Domain



# Create your models here.
class Student(models.Model):

    STATUS=(
    ('Training','Training'),
    ('Placed','Placed'),
    ('RequestedTermination','RequestedTermination'),
    ('Terminated','Terminated'),
    ('Quit','Quit'),
    )
    FEE = (
        ('Upfront','Upfront'),
        ('ISI','ISI'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    batch= models.ForeignKey(Batch, on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=20,choices=STATUS)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,null=True)
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL,null=True)
    domain = models.ForeignKey(Domain, on_delete=models.SET_NULL,null=True, blank=True)
    fee = models.CharField(max_length=20,choices=FEE,default='ISI')

    def __str__(self):
        s = self.user.username + ' ' + str(self.id)
        return s

class Placement(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    position = models.CharField(max_length=20,null=True, blank=True)
    company = models.CharField(max_length=30,null=True, blank=True)
    location = models.CharField(max_length=20,null=True, blank=True)
    LPA = models.FloatField()
    address = models.TextField(null=True, blank=True)
    count = models.IntegerField(null=True)
    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.student.user.username

class Shifted(models.Model):
    student= models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    shifted_to = models.ForeignKey(Batch, on_delete=models.SET_NULL,null=True,blank=True)
    shifted_from = models.ForeignKey(Batch, on_delete=models.SET_NULL,null=True,blank=True,related_name="come_from")
    created= models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.student.user.username
    

class Attendance(models.Model):
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    stcode = models.ManyToManyField(Student)

class EducationDetails(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    education = models.CharField(max_length=225, null=True)
    stream = models.CharField(max_length=225, null=True)
    courses = models.TextField(null=True)
    backlogs = models.CharField(max_length=225, null=True)
    experience = models.BooleanField(default=False)
    company = models.CharField(max_length=225, null=True)
    duration = models.CharField(max_length=225, null=True)