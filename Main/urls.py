from django.urls import path
from .views import (
    DepartmentView,
    EquipmentView,
    ManufacturerView,
    ProductView,
    UserView,
    ProductGranulationView,
    RoomView
)

urlpatterns = [
    path("departments", DepartmentView.as_view()),
    path("products", ProductView.as_view()),
    path("equipments", EquipmentView.as_view()),
    path("manufacturers", ManufacturerView.as_view()),
    path("users", UserView.as_view()),
    path("product-details", ProductGranulationView.as_view()),
    path("rooms", RoomView.as_view())
]
