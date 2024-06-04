"""
URL configuration for mydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mydjango import views
urlpatterns = [
    path("admin/", admin.site.urls),
    # path("course/<int:courseid>",views.course),
    path("",views.home),
    path("aboutus/",views.aboutus),   
    #path("aboutus/",views.aboutus,name="about"), url method
    #  <li><a href="{% url 'about' %}">About Us</a></li> use this in header.html for url method
    # path("submitform/",views.submitform,name="submitform"),
    path("contact/",views.contact),
    path("services/",views.services),
    # path("userform/",views.forms),
    path("calculator/",views.calculator)


    # create a url to render the content of views in browser
]
