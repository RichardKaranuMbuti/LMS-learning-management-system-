from django.urls import path
from . import views

urlpatterns = [
   
    path('department/create/', views.create_department, name='create_department'),
    path('unit/create/', views.create_unit, name='create_unit'),
]
