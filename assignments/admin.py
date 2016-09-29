from django.contrib import admin

# Register your models here.
from assignments.models import Assignment,Question,Answers

admin.site.register(Assignment)
admin.site.register(Question)
admin.site.register(Answers)