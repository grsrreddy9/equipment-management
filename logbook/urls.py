from django.urls import path
from .views import LogBookView
urlpatterns = [
    path('', LogBookView.as_view()),
]
