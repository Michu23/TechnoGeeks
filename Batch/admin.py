from django.contrib import admin
from .models import Batch, Branch, Group
# Register your models here.

admin.site.register(Batch)
admin.site.register(Group)
admin.site.register(Branch)