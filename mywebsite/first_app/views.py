from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    dict={'insert_me':"Hello hello!"}
    return render(request,'first_app/index.html',context=dict)
