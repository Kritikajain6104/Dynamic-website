from django.db import models

# Create your models here.
class lead(models.Model):
    lead_name=models.CharField(max_length=50)
    lead_twitter=models.URLField(max_length=200,default='some_value')
    lead_insta=models.URLField(max_length=200,default='some_value')
    lead_linkedin=models.URLField(max_length=200,default='some_value')
    lead_teamname=models.CharField(max_length=50)
    lead_image=models.FileField(upload_to="",max_length=250,default=None,null=True)