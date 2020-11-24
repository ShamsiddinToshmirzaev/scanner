from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin

from .models import Target, Scan_Type, Scan, Result


class TargetAdmin(admin.ModelAdmin):
    list_display = ('id', 'target', 'type', 'user',)
    list_display_links = ('target',)


class ScanTypeAdmin(admin.ModelAdmin):
    # MPTT_ADMIN_LEVEL_INDENT = 30
    list_display = ('id', 'name', 'parent')
    list_display_links = ('name',)


class ScanAdmin(admin.ModelAdmin):
    list_display = ('id', 'target', 'scan_type', 'start_date', 'status', 'progress', 'command')


class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'xml', 'json',)
    list_display_links = ('xml', 'json')


admin.site.register(Target, TargetAdmin)
admin.site.register(Scan_Type, ScanTypeAdmin)
admin.site.register(Scan, ScanAdmin)
admin.site.register(Result, ResultAdmin)
