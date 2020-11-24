from django.urls import path
from . import views

urlpatterns = [
    path('type/', views.apiOverview, name="api-overview"),
    path('type-list/', views.typeList, name="type-list"),
    path('type-detail/<str:pk>/', views.typeDetail, name="type-detail"),
    path('type-create/', views.typeCreate, name="type-create"),
    path('type-update/<str:pk>/', views.typeUpdate, name="type-update"),
    path('type-delete/<str:pk>/', views.typeDelete, name="type-delete"),
]
