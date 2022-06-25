from django.db import models
from Student.models import Student
from Admin.models import Advisor, Reviewer


# Create your models here.


class Manifest(models.Model): 
    title = models.CharField(max_length = 7, default = '')
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    personal_wo = models.TextField(null=True, default = '')
    misc_wo = models.TextField(null=True, default = '')
    technical_score = models.IntegerField(null=True, default = 0)
    misc_score = models.IntegerField(null=True, default = 0)
    is_complete = models.BooleanField(default=False)
    next_review = models.DateField(null=True)
    folder = models.CharField(max_length = 255, default = '')

    def __str__(self):
        name = self.title + ' of ' + self.student_name.user.username + ' ' + str(self.id)
        return name

class Review(models.Model):
    STATUS = (
        ('Task Completed','Task Completed'),
        ('Need Improvement','Need Improvement'),
        ('Task Critical','Task Critical'),
        ('Repeat Review','Repeat Review'),
        )
    created = models.DateField(auto_now_add=True)
    manifest = models.ForeignKey(Manifest, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.SET_NULL, null=True, blank=True)
    advisor = models.ForeignKey(Advisor,  on_delete=models.SET_NULL, null=True, blank=True)
    remark = models.TextField(null=True, default = '')
    status = models.CharField(max_length=20, choices=STATUS, default='')

    def __str__(self):
        name = self.manifest.student_name.user.username + "'s review on "
        return name

class Tasks(models.Model):
    week = models.ForeignKey(Manifest,on_delete=models.CASCADE,null=True)
    taskname = models.CharField(max_length=20,null=True,blank=True)
    status =models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.taskname

class DataStructure(models.Model):
    userid = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=20,null=True,blank=True)
    status = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class DS_Review(models.Model):
    created = models.DateField(auto_now_add=True)
    ds = models.ForeignKey(DataStructure, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length = 20,null=True)
    remark = models.TextField(null=True)

    def __str__(self):
        return str(self.date.date())
    







