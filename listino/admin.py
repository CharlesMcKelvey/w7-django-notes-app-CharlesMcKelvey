from django.contrib import admin
from listino.models import Note, NoteItem

# Register your models here.


class NoteItemInline(admin.TabularInline):
    model = NoteItem
    extra = 3


class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'updated_at',
        'created_at'
    )

    inlines = [NoteItemInline]


admin.site.register(Note, NoteAdmin)
admin.site.register(NoteItem)
