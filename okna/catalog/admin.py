from django.contrib import admin
from .models import Group, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'text',
        'group',
    )
    list_editable = ('group', 'text')
    search_fields = ('text',)
    empty_value_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
admin.site.register(Group)