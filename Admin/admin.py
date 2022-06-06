from django.contrib import admin
from .models import Advisor, Reviewer, Code
# Register your models here.

admin.site.register(Advisor)
admin.site.register(Reviewer)
admin.site.register(Code)