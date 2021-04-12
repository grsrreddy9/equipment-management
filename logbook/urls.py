from django.urls import path
from .views import LogBook
urlpatterns = [
    path('data', LogBook.as_view()),
]
