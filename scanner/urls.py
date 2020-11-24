from django.urls import path
from . import views

urlpatterns = [
    path('type/', views.apiOverview, name="api-overview"),
    path('type-list/', views.typeList, name="type-list"),
    path('type-detail/<str:pk>/', views.typeDetail, name="type-detail"),
    path('type-create/', views.typeCreate, name="type-create"),
    path('type-update/<str:pk>/', views.typeUpdate, name="type-update"),
    path('type-delete/<str:pk>/', views.typeDelete, name="type-delete"),

    #      for result model
    path('result-list/', views.resultList, name="result-list"),
    path('result-detail/<str:pk>/', views.resultDetail, name="result-detail"),
    path('result-create/', views.resultCreate, name="result-create"),
    path('result-update/<str:pk>/', views.resultUpdate, name="result-update"),
    path('result-delete/<str:pk>/', views.resultDelete, name="result-delete"),


]

