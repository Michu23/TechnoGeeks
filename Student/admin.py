from django.contrib import admin
from .models import Student, Placement, Shifted,Attendance
# Register your models here.


admin.site.register(Attendance)
admin.site.register(Student)
admin.site.register(Placement)
admin.site.register(Shifted)