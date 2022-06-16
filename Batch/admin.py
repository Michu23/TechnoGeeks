from django.contrib import admin
from .models import Batch, Group, Location, Branch
# Register your models here.

admin.site.register(Batch)
admin.site.register(Group)
admin.site.register(Location)
admin.site.register(Branch)