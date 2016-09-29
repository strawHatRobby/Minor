from django.contrib import admin

# Register your models here.
from forums.models import Form,Comments

admin.site.register(Form)
admin.site.register(Comments)