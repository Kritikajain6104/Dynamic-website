from django.db import models

# Create your models here.
class eventteam(models.Model):
    et_name=models.CharField(max_length=50)
    # tt_twitter=models.URLField(max_length=200,default='some_value')
    et_insta=models.URLField(max_length=200,default='some_value')
    et_linkedin=models.URLField(max_length=200,default='some_value')
    et_teamname=models.CharField(max_length=50)
    et_image=models.FileField(upload_to="",max_length=250,default=None,null=True)
    et_shortdesc=models.TextField()