from django.contrib import admin
from .models import Block, Apartment
from .forms import ApartmentForm, BlockForm

@admin.display(description='total cost')
def total_cost(obj):
    total_cost = int(obj.total_area * obj.block.cost_per_sq_meter)
    return total_cost

class ApartmentAdmin(admin.ModelAdmin):
    form = ApartmentForm
    list_display = ('owner_name', 'status','block', 'purchase_date', total_cost)
    list_editable = ('purchase_date',)
    date_hierarchy = 'owner_birthdate'
    #list_display_links = ('block',)
    list_filter = ('block', 'status')
    search_fields = ('owner_name',)
    fields = ('owner_name', 'purchase_date', 'owner_birthdate', 'status', 'total_area')

class BlockAdmin(admin.ModelAdmin):
    list_display = ('block_number', 'entrance_number', 'floor_number', 'apartment_number_per_floor', 'cost_per_sq_meter', 'total_number_apartments','total_cost_apartments')
    
    @admin.display(description='Total number of all apartments')
    def total_number_apartments(self, obj):
        total_number_apartments = int(obj.entrance_number * obj.floor_number * obj.apartment_number_per_floor)
        return total_number_apartments
    
    @admin.display(description='Total cost of all apartments')
    def total_cost_apartments(self, obj):
        total_cost_apartments = int(obj.entrance_number * obj.floor_number * obj.apartment_number_per_floor * obj.cost_per_sq_meter)
        return total_cost_apartments

admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Block, BlockAdmin)



