from django.contrib import admin
from .models import LogBook, CleanType, CleaningDetail

class LogBookAdmin(admin.ModelAdmin):
    pass

class CleanTypeAdmin(admin.ModelAdmin):
    pass

class CleaningDetailAdmin(admin.ModelAdmin):
    pass


admin.site.register(LogBook, LogBookAdmin)
admin.site.register(CleanType, CleanTypeAdmin)
admin.site.register(CleaningDetail, CleaningDetailAdmin)

# Register your models here.
