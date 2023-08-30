from django.contrib import admin
from techteam.models import techteam

# Register your models here.
class techteamAdmin(admin.ModelAdmin):
    list_display=('tt_name','tt_teamname','tt_insta','tt_linkedin','tt_image','tt_shortdesc')


admin.site.register(techteam,techteamAdmin)    