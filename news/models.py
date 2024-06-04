from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class News(models.Model):
    # please setup tinymce and news in settings
   news_title=models.CharField(max_length=34)
   news_desc=HTMLField()