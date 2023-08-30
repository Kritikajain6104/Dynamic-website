from django.db import models

# Create your models here.
class gdteam(models.Model):
    gt_name=models.CharField(max_length=50)
    # tt_twitter=models.URLField(max_length=200,default='some_value')
    gt_insta=models.URLField(max_length=200,default='some_value')
    gt_linkedin=models.URLField(max_length=200,default='some_value')
    gt_teamname=models.CharField(max_length=50)
    gt_image=models.FileField(upload_to="",max_length=250,default=None,null=True)
    gt_shortdesc=models.TextField()