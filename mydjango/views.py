from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userforms

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
    #  as soon as aboutus page is requested, this function is called
    # this function gets the output passed in url and render to the aboutus page
     if request.method=='GET':
        output=request.GET.get('output')
     return render(request,"aboutus.html",{'output':output})
def contact(request):
     return render(request,"contact.html")
def services(request):
     return render(request,"service.html")
def submitform(request):
     
    #  form take data to the url as mentioned in the action of the form
    # url in the action of the form call this function
     data={}
     try:
          if request.method=="POST":
            name=request.POST.get('names')
            email=request.POST.get('email')
            password=request.POST.get('password')
            data={
                'name':name,
                'email':email,
                'password':password
            }
            return HttpResponse(email)
        #   the name would be responded to the submitform page
     except:
       pass
    
def forms(request):
     fn=userforms()
    #  creating form using django form
     data={'form':fn}
    
    #  defining the dictionary
     try:
        #   if request.method=="GET":
          if request.method=="POST":
            name=request.POST.get('names')
            email=request.POST.get('email')
            password=request.POST.get('password')
            data={
                'form':fn,
                'name':name,
                'email':email,
                'password':password
            }
            url="/aboutus/?output={}".format(name)
            # send the ouput too to the redirected page in url
            return HttpResponseRedirect(url)
        #   for redirecting to some page just after submitting the form
        
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