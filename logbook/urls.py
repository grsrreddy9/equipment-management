from django.urls import path
from .views import LogBookView, CleanTypeView
urlpatterns = [
    path('', LogBookView.as_view()),
    path('clean-types', CleanTypeView.as_view())
]
