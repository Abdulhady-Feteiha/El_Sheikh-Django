from django.contrib import admin
from .models import machine
from django.shortcuts import render,HttpResponseRedirect
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class MachineResource(resources.ModelResource):
    
    class Meta:
        model = machine
class MachineAdmin(admin.ModelAdmin):
    # list_display = ['Machine_TYPE', 'Location','Mark', 'Features', 'Mama','Yousra','Abdullah','Abdulhady','Mohamed','purchase_date','purchase_price','sell_date','sell_price',]
    list_display = ['Machine_TYPE', 'Location','Mark', 'Features','Owners','purchase_date','purchase_price','sell_date','sell_price',]

    ordering = ['purchase_date']
    search_fields = ['Machine_TYPE', 'Location','Mark', 'Features','Owners','purchase_date','purchase_price','sell_date','sell_price',]
    resource_class = MachineResource


admin.site.register(machine,MachineAdmin)

