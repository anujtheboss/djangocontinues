from django.db import models
# add the service app in installed app list of settings.py
# command to create model::python manage.py startapp service
# command to make migrations:python manage.py makemigrations
# command to convert the model to table:python manage.py migrate(db will be created)
# Create your models here.
class Service(models.Model):
    # model provide the interface for interacting with database
    service_icon=models.CharField(max_length=30)
    service_title=models.CharField(max_length=30)
    service_des=models.TextField()

# migrations helps to track the changes over the model(model describe the structure of database) over time