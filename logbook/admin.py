from django.contrib import admin
from .models import LogBook, CleanType

class LogBookAdmin(admin.ModelAdmin):
    pass

class CleanTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(LogBook, LogBookAdmin)
admin.site.register(CleanType, CleanTypeAdmin)

# Register your models here.
