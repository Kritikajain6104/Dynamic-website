from django.contrib import admin
from eventteam.models import eventteam
# Register your models here.
class eventteamAdmin(admin.ModelAdmin):
    list_display=('et_name','et_insta','et_linkedin','et_teamname','et_image','et_shortdesc')


admin.site.register(eventteam,eventteamAdmin)    