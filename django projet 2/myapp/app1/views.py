from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render(request,"login.html")
def kurslar(request):
    return HttpResponse('kurs listesi')
