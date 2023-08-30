from django.contrib import admin
from contentteam.models import contentteam
# Register your models here.
class contentteamAdmin(admin.ModelAdmin):
    list_display=('ct_name','ct_teamname','ct_insta','ct_linkedin','ct_image','ct_shortdesc')

admin.site.register(contentteam,contentteamAdmin)    