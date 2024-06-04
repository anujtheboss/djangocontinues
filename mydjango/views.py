from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userforms
from service.models import Service

# some times while changing the name of the model again perform the migrations to reflect it in admin
def home(request):
     return render(request,"index.html")
# http response cant call the page but render can
def aboutus(request):
    #  as soon as aboutus page is requested, this function is called
    # this function gets the output passed in url and render to the aboutus page
     if request.method=='GET':
        output=request.GET.get('output')
     return render(request,"aboutus.html",{'output':output})
def contact(request):
     return render(request,"contact.html")
def services(request):
    #  extracting data from db and rendering to service.html page
    #  service_data=Service.objects.all()
    #  service_data=Service.objects.all().order_by("service_icon")  #ascending
     service_data=Service.objects.all().order_by("-service_icon")  #descending
    #  service_data=Service.objects.all().order_by("service_icon")[:3]  #extracting only 3 data


    #  data={
    #      'serviceData':serviceData
    #  }

     return render(request,"serve.html",{'serviceData':service_data})
# def submitform(request):
#      data={}
#      try:
#           if request.method=="POST":
#             name=request.POST.get('names')
#             email=request.POST.get('email')
#             password=request.POST.get('password')
#             data={
#                 'name':name,
#                 'email':email,
#                 'password':password
#             }
#             return HttpResponse(email)
#         #   the name would be responded to the submitform page
#      except:
#        pass
    

def calculator(request):
    try:
        c=''
        if request.method=='POST':
            n1=eval(request.POST.get('value1'))
            n2=eval(request.POST.get('value2'))
            op=request.POST.get("operator")
            if op=='+':
               c=n1+n2
            elif op=='-':
               c=n1-n2
            elif op=='*':
               c=n1*n2
            else:
               c=n1/n2
    except:
        c='invalid'
    return render(request,"calculator.html",{"c":c})

