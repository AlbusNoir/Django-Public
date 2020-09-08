from django.contrib import admin

from learning_logs.models import Topic, Entry

from django_summernote.admin import SummernoteModelAdmin

from .models import Entry

class EntryAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

admin.site.register(Topic)
admin.site.register(Entry, EntryAdmin)

