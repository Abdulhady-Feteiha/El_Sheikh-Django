import os 
import sys
from math import floor
from datetime import date
from pathlib import Path
from django.core import serializers
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Path(BASE_DIR).parent.absolute())
from config import *

def Make_a_report(machine,transaction,Owner,Month,Year):
    all_sold_machines = machine.objects.filter(sell_date__isnull=False,Owners__contains=Owner)
    all_purchased_machines = machine.objects.filter(purchase_date__isnull=False,Owners__contains=Owner)
    
    current_sold_machines = machine.objects.filter(sell_date__year__gte=Year,sell_date__month__gte=Month,sell_date__year__lte=Year,sell_date__month__lte=Month,Owners__contains=Owner)
    current_purchased_machines = machine.objects.filter(purchase_date__year__gte=Year,purchase_date__month__gte=Month,purchase_date__year__lte=Year,purchase_date__month__lte=Month,Owners__contains=Owner)
    
    all_Profit, all_Investment,_ = compute_finance(all_sold_machines,all_purchased_machines,Owner)
    current_Profit, current_Investment,Surplus = compute_finance(current_sold_machines,current_purchased_machines,Owner)

    all_current_Machines = current_sold_machines.union(current_purchased_machines)
    all_current_machines_data = serializers.serialize( "python", all_current_Machines )

    all_transactions = transaction.objects.filter(Owner__contains=Owner)
    current_transactions = transaction.objects.filter(Date__year__gte=Year,Date__month__gte=Month,Owner__contains=Owner)
    transaction_data =  serializers.serialize( "python", current_transactions )

    Total_in_stock = compute_transaction(all_transactions,Owner,Month,Year,all_Profit,all_Investment)
    return all_Profit, all_Investment,current_Profit, current_Investment, Total_in_stock, all_current_machines_data,transaction_data,Surplus

def compute_finance(sold_machines,purchased_machines,Owner):
    Investment = 0
    Profit = 0
    Surplus = 0
    if sold_machines:
        for m in sold_machines:
            Profit = Profit + compute_percentage(Owner,m,"Sell")
            if m.purchase_price:
                Surplus = Surplus + compute_percentage(Owner,m,"Sell") - compute_percentage(Owner,m,"Purchase")
    else:
        Profit = "لم يتم بيع أي ماكينات في هذا الشهر"
    if purchased_machines:
        for m in purchased_machines:
            Investment = Investment + compute_percentage(Owner,m,"Purchase")
    else:
        Investment = "لم يتم شراء أي ماكينات في هذا الشهر"
    return Profit,Investment,Surplus

def compute_percentage(Owner,machine,operation):
    if operation=="Sell":
        if machine.purchase_date<date(2021,6,1):
            profit = machine.sell_price*percent_dict[Owner]
        else:
            owners_list = str(machine.Owners).split(',')
            profit = machine.sell_price/len(owners_list)
        return floor(profit)
    elif operation=="Purchase":
        if machine.purchase_date<date(2021,6,1):
            investment = 0
        else:
            owners_list = str(machine.Owners).split(',')
            investment = machine.purchase_price/len(owners_list)
        return floor(investment)
    else:
        raise Exception("Unidentified operation")

def compute_transaction(all_transactions,Owner,Month,Year,Profit,Investment):
    Total_in_stock = Profit-Investment
    for t in all_transactions:
        if t.Operation == Operations[0][0]:
            Total_in_stock = Total_in_stock-t.Amount
        else:
            Total_in_stock = Total_in_stock+t.Amount
    return Total_in_stock