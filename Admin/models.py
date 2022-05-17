from django.db import models
from User.models import User, Profile

# Create your models here.
class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)

