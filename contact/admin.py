from django.contrib import admin
from contact.models import contact1
# Register your models here.

class contactadmin(admin.ModelAdmin):
    list_display=('first_name','last_name','Email','message')


admin.site.register(contact1,contactadmin)