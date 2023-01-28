from django.contrib import admin
from blog.models import blog
# Register your models here.
class blogadmin(admin.ModelAdmin):
    list_display=('blog_name','blog_shortdecs','blog_desc')

admin.site.register(blog,blogadmin)    