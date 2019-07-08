from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'town', 'cardinal_point')
    list_filter = ('town', 'cardinal_point')
    search_fields = ['name', 'town', 'cardinal_point']


admin.site.register(Location, LocationAdmin)
admin.site.site_header = "TT Flood Relief Admin Panel";
admin.site.site_title = "TT Flood Relief Admin Panel";
