from django.contrib import admin
from .models import User, Department, Equipment, Room, Product, ProductGranulation


class DepartmentAdmin(admin.ModelAdmin):
    pass


# class ManufacturerAdmin(admin.ModelAdmin):
#     pass


class EquipmentAdmin(admin.ModelAdmin):
    pass


class RoomAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductGranulationAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Department, DepartmentAdmin)
# admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGranulation, ProductGranulationAdmin)
admin.site.register(User, UserAdmin)
