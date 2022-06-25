from django.db import models
from User.models import User, Profile

# Create your models here.

class Location(models.Model):
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.place

class Lead(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.user.username + str(self.id)

class Reviewer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Code(models.Model):
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.code