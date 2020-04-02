
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    myobj = {'name':'John Doe'}
    return render(request,'index.html',myobj)


def help(request):
    return render(request,'help.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')