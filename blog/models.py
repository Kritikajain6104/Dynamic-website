from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class blog(models.Model):
    blog_name=models.CharField(max_length=100)
    blog_shortdecs=models.TextField()
    blog_desc=HTMLField()

