from django.db import models
from User.models import User, Profile

# Create your models here.
class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)

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