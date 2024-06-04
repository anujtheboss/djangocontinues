from django.contrib import admin
from service.models import Service
# Register your models here.
class serviceadmin(admin.ModelAdmin):
    list_display=['service_icon','service_title','service_des']
admin.site.register(Service,serviceadmin)
# registering the model to the admin site to display the field and data

# to access the admin panel create superuser::password:anyouzboss@345 email:anujth345@gmail.com
# go to the browser and type:localhost:8000/admin