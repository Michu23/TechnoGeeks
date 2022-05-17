from django.db import models
from User.models import User
from Student.models import Student


# Create your models here.


class Manifest(models.Model): #week
    title = models.CharField(max_length = 7)
    student_name = models.ForeignKey(Student, on_delete=models.SET_NULL,null=True)
    next_review = models.DateTimeField(null=True)
    personal_wo = models.TextField(null=True)
    misc_wo = models.TextField(null=True)
    techical_score = models.IntegerField(null=True)
    misc_score = models.IntegerField(null=True)
    is_complete = models.BooleanField(default=False)

class Review(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    manifest = models.ForeignKey(Manifest, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length = 20,null=True)
    remark = models.TextField(null=True)

class Tasks(models.Model):
    week = models.ForeignKey(Manifest,on_delete=models.SET_NULL,null=True)
    taskname = models.CharField(max_length=20,null=True,blank=True)
    status =models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

class DataStructure(models.Model):
    userid = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=20,null=True,blank=True)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

class DS_Review(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    ds = models.ForeignKey(DataStructure, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length = 20,null=True)
    remark = models.TextField(null=True)
    







