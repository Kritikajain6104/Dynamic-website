from django.contrib import admin
from gdteam.models import gdteam
# Register your models here.
class gdteamAdmin(admin.ModelAdmin):
    list_display=('gt_name','gt_insta','gt_linkedin','gt_teamname','gt_image','gt_shortdesc')


admin.site.register(gdteam,gdteamAdmin)    