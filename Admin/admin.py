from django.contrib import admin
from .models import Advisor, Reviewer, Code, Lead, Location
# Register your models here.

admin.site.register(Advisor)
admin.site.register(Reviewer)
admin.site.register(Code)
admin.site.register(Lead)
admin.site.register(Location)