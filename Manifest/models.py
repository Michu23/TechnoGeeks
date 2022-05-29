from django.db import models
from Student.models import Student


# Create your models here.


class Manifest(models.Model): 
    title = models.CharField(max_length = 7, default = '')
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    personal_wo = models.TextField(null=True, default = '')
    misc_wo = models.TextField(null=True, default = '')
    techical_score = models.IntegerField(null=True, default = 0)
    misc_score = models.IntegerField(null=True, default = 0)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        name = self.title + ' of ' + self.student_name.user.username + ' ' + str(self.id)
        return name

class Review(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    manifest = models.ForeignKey(Manifest, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length = 20,null=True, default = '')
    remark = models.TextField(null=True, default = '')
    next_review = models.DateTimeField(null=True)

    def __str__(self):
        name = self.manifest.student_name.user.username + "'s review on " + str(self.date.date()) 
        return name

class Tasks(models.Model):
    week = models.ForeignKey(Manifest,on_delete=models.CASCADE,null=True)
    taskname = models.CharField(max_length=20,null=True,blank=True)
    status =models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskname

class DataStructure(models.Model):
    userid = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=20,null=True,blank=True)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class DS_Review(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    ds = models.ForeignKey(DataStructure, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length = 20,null=True)
    remark = models.TextField(null=True)

    def __str__(self):
        return str(self.date.date())
    







