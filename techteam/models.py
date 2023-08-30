from django.db import models

# Create your models here.
class techteam(models.Model):
    tt_name=models.CharField(max_length=50)
    # tt_twitter=models.URLField(max_length=200,default='some_value')
    tt_insta=models.URLField(max_length=200,default='some_value')
    tt_linkedin=models.URLField(max_length=200,default='some_value')
    tt_teamname=models.CharField(max_length=50)
    tt_image=models.FileField(upload_to="",max_length=250,default=None,null=True)
    tt_shortdesc=models.TextField()