from django.urls import path
from .views import (
    DepartmentView,
    EquipmentView,
    ManufacturerView,
    ProductView,
    UserView,
    ProductGranulationView
)

urlpatterns = [
    path("department", DepartmentView.as_view()),
    path("product", ProductView.as_view()),
    path("equipment", EquipmentView.as_view()),
    path("manufacturers", ManufacturerView.as_view()),
    path("users", UserView.as_view()),
    path("product-details", ProductGranulationView.as_view()),
]
