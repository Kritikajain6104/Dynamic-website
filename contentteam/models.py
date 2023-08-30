from django.db import models

# Create your models here.
class contentteam(models.Model):
    ct_name=models.CharField(max_length=50)
    # tt_twitter=models.URLField(max_length=200,default='some_value')
    ct_insta=models.URLField(max_length=200,default='some_value')
    ct_linkedin=models.URLField(max_length=200,default='some_value')
    ct_teamname=models.CharField(max_length=50)
    ct_image=models.FileField(upload_to="",max_length=250,default=None,null=True)
    ct_shortdesc=models.TextField()