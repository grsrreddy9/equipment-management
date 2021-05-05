from django.urls import path
from .views import LogBookView, CleanTypeView, CleaningDetailsView
urlpatterns = [
    path('', LogBookView.as_view()),
    path('clean-types', CleanTypeView.as_view()),
    path('cleaning', CleaningDetailsView.as_view())
]
