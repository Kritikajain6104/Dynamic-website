from django.contrib import admin
from lead.models import lead


# Register your models here.
class leadadmin(admin.ModelAdmin):
    list_display=('lead_name','lead_teamname','lead_insta','lead_twitter','lead_linkedin','lead_image')


admin.site.register(lead,leadadmin)    