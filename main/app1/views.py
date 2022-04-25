from cgitb import text
from rest_framework import viewsets
from multiprocessing import context
from unicodedata import name
from django import template
from django.shortcuts import render
from django.template import loader
from .forms import Employeeform , Form
# Create your views here.
from django.http import HttpResponse, JsonResponse
from app1 import models
from app1 import serializer

def showme(request):
    text= """<h1> welcome to my app!</h1>"""
    return HttpResponse(text)


def index(request):
    template = loader.get_template('index.html')
    name = {
        'name':'Suraj'
    }
    return HttpResponse(template.render(name))

# def home(request):
#     context={}
#     context["name"]="Mark"
#     context['myform']=Employeeform
#     return render(request,"index.html",context)


def home(request):
    if request.method == "POST":
        form=Employeeform(request.POST)
        if form.is_valid():
            try:
                return render(request,'page1.html',{'username':"Suraj"})
                # return redirect ("/page1")
            except:
                pass
    else:
        form=Employeeform()
    return render (request,'index.html',{'form':form})

    # date format is 15/05/2021

import os
def Form(request):
    if request.method=='POST':
        student = Form(request.POST, request.FILES)
        if student.is_valid():
            f = request.FILES['file']
            path = 'app/upload/'
            if not os.path.exists(path):
                os.mkdir(path)
            try:
                with open(path + f.name, 'wb+') as destination:
                    for data in f.chunks():
                        destination.write(data)
                        return HttpResponse("File uploadedf successfully")
            except:
                pass
    else:
        form = Form()
        return render(request, "index.html", {'form': form})


def create_view(request):
    context = {}
    form = Employeeform(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request, "emp_view.html", context)    



def data_view(request):
    context={}
    context["dataset"]=models.Employee.objects.all()
    return render(request, "data_view.html", context)


def detail_view(request, id):
    context = {}
    context["dataobj"] = models.Employee.objects.get(id=id)
    return render(request, "detail_view.html", context)

class EmpViewSet(viewsets.ViewSet):
    def list(self,request):
        emps=models.Employee.objects.select_related('department').prefetch_related("project").all()
        serializer=serializer.EmployeeSerializer(emps,many=True)
        print(serializer)
        return JsonResponse(serializer.data,safe=False)

    def create(self,request):
        data= JSoNParser().parse(request)
        serializer=serializer.EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,ststus=400)
