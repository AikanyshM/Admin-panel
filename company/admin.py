from django.contrib import admin

from django.contrib import admin
from .models import Block, Apartment

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('owner_name', 'status','block', 'purchase_date')
    list_editable = ('purchase_date',)
    date_hierarchy = 'owner_birthdate'
    list_display_links = ('block',)
    list_filter = ('block', 'status')
    search_fields = ('owner_name',)

class BlockAdmin(admin.ModelAdmin):
    list_display = ('block_number',)

admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Block, BlockAdmin)



