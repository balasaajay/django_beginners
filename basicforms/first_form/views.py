from django.shortcuts import render
from . import forms
# Create your views here.


def index(request):
    return render(request,'first_form/index.html')

def form_name_view(request):
    form = forms.FormName()
    return render(request,'first_form/form_disp.html', {'form': form})
