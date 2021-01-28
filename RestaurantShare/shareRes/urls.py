# shareRes > urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail),
    path('restaurantCreat/', views.restaurantCreat),
    path('categoryCreate/', views.categoryCreate)
]