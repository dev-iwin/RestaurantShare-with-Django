from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sendEmail(request):
    return HttpResponse("sendEmail")  # 우선 단순 문자열 출력, 추후 로직 구성