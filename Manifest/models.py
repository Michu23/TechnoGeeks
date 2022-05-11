from django.db import models
from User.models import User


# Create your models here.


class Manifest(models.Model):
    title = models.CharField(max_length = 7)
    date= models.DateTimeField(auto_now_add=True)
    personal_wo = models.TextField()
    misc_wo = models.TextField()
    techical_score = models.IntegerField()
    misc_score = models.IntegerField()
    english = models.TextField()



class Tasks(models.Model):
    userid= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    week= models.ForeignKey(Manifest,on_delete=models.SET_NULL,null=True)
    taskname= models.CharField(max_length=20,null=True,blank=True)
    status=models.BooleanField(default=False)
    date= models.DateTimeField(auto_now_add=True)
    







