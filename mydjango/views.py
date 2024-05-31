from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def home(request):
                                                    #  the request is from the home/ url
                                                #      data={
                                                #      'title':'homepage',
                                                #      'clist':['samsung','redmi','iphone'],
                                                #      'student':[
                                                #           {'name':'dinesh','phone':32454656},
                                                #           {'name':'ram','phone':92537975}
                                                #      ]
                                                # }
                                                    # to pass some variable from django page to html
     return render(request,"index.html")
# http response cant call the page but render can
def aboutus(request):
     return render(request,"aboutus.html")
def contact(request):
     return render(request,"contact.html")
def services(request):
     return render(request,"service.html")
def forms(request):
     data={}
    #  defining the dictionary
     try:
        #   if request.method=="GET":
          if request.method=="POST":
            name=request.POST.get('names')
            email=request.POST.get('email')
            password=request.POST.get('password')
            data={
                'name':name,
                'email':email,
                'password':password
            }
            return HttpResponseRedirect("/aboutus/")
     except:
       pass
     return render(request,"userform.html",data)
# in userform we can directly access the value using the key

# 

# slug> sdf-ad-sdf-sf

# for dynamic url
def course(request,courseid):
     return HttpResponse(courseid)

# http request method =post,get,delete,update.....

# the page url and encoded information in the url is separated by ? mark
# get method send the encoded user information appended to the page request
# size limit
# GET method is not safe

# POST method transfer information via http headers
# no data size limit
# security depend on http protocol