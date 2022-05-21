from django.contrib import admin

from .models import User, Department, Domain, Profile, Notification
# Register your models here.

admin.site.register(User)
admin.site.register(Department)
admin.site.register(Domain)
admin.site.register(Profile)
admin.site.register(Notification)