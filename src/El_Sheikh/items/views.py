from django.shortcuts import render
from transactions.models import Item
from config import *

def Items(request):
    Machine_list = Item.objects.order_by('-Owner')
    context = {
        'Machine_list': Machine_list,

    }
    return render(request,'show_items.html',context)
    #return HttpResponse(output)

