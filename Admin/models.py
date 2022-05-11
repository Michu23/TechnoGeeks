from django.db import models
from User.models import Profile

# Create your models here.
class Advisor(models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE)

