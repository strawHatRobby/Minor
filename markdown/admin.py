from django.contrib import admin

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}