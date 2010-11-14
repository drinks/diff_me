from django.contrib import admin
from diff_me.main.models import *

class DiffAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ('__unicode__', 'timestamp', 'private')
    search_fields = ('base58_id', 'original', 'original_revision', 'modified', 'modified_revision')
admin.site.register(Diff, DiffAdmin)