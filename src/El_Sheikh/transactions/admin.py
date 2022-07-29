from django.contrib import admin
from .models import transaction
from django.shortcuts import render,HttpResponseRedirect

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['Owner', 'Date','Amount','Operation',]
    ordering = ['Owner']
    search_fields = ['Owner', 'Date','Amount','Operation',]
  
admin.site.register(transaction,TransactionAdmin)

# Register your models here.
