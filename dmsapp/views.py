from django.shortcuts import render
from importlib.metadata import requires

def login(request):
    return render(request,'login.html')
def index(request):
    return render(request,'index.html')
def forgot(request):
    return render(request,'forgot-password.html')
def createlog(request):
    return render(request,'register.html')
def table(request):
    return render(request,'tables.html')
def chart(request):
    return render(request,'charts.html')