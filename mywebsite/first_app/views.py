from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from first_app.models import User
#def index(request):
#    dict={'insert_me':"Hello hello!"}
#    return render(request,'first_app/index.html',context=dict)

def index(request):
    return render(request, 'first_app/index.html')

def users(request):
    users_list=User.objects.all()
    # users_list=User.objects.order_by('first_name')
    dict={'users': users_list}
    return render(request,'first_app/usersdisp.html',context=dict)
