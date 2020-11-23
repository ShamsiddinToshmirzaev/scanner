from django.urls import path

from .views import ScanTypeView


app_name = "scanner"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('types/', ScanTypeView.as_view()),
    path('types/<int:pk>', ScanTypeView.as_view())
]
