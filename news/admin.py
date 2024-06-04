from django.contrib import admin
from news.models import News
class modeladmin(admin.ModelAdmin):
    list_display=['news_title','news_desc']
admin.site.register(News,modeladmin)
# Register your models here.


# python manage.py makemigrations
# python manage.py migrate