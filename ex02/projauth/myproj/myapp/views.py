from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .models import Student,lab
# Create your views here.


def home(request):
    return render(request,"myapp/home.html")


0@login_required(login_url='/accounts/login')
def students(request):
    qr=Student.objects.all()
    context={'qres':qr}
    return render(request,"students.html",context)




@permission_required('myapp.view_labs')
def view_labs(request):
    qr=lab.objects.all()
    context={'qres':qr}
    return render(request,"myapp/labs.html",context)
