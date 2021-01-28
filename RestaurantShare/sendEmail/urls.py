# sendEmail > urls.py
from django.urls import path, include
from . import views  # 같은 경로에서 views 파일을 임포트

urlpatterns = [
    path('send/', views.sendEmail)  # 사용자의 요청에 대해 views의 sendEmail함수로 처리를 넘김 
]