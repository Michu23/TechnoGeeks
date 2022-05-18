from django.contrib import admin
from .models import Manifest, Review, Tasks, DataStructure, DS_Review
# Register your models here.

admin.site.register(Manifest)
admin.site.register(Review)
admin.site.register(Tasks)
admin.site.register(DataStructure)
admin.site.register(DS_Review)