# sendEmail > urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('send/', views.sendEmail)  # 사용자의 요청에 대해 views의 sendEmail함수로 처리를 넘김 
]