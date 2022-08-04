from django.shortcuts import render,HttpResponseRedirect
from .forms import report_request_Form
from .pages_utils import Make_a_report
from Machine.models import machine
from Transactions.models import transaction
def home(request):
   return render(request, "home.html", {})

def Report_request(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = report_request_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            Owner = form.cleaned_data['Owner']
            Month = form.cleaned_data['Month']
            Year = form.cleaned_data['Year']
            machine_fields = [f.name for f in machine._meta.get_fields()]
            machine_fields.pop(0)
            transaction_fields = [f.name for f in transaction._meta.get_fields()]
            transaction_fields.pop(0)
            all_Profit, all_Investment,current_Profit, current_Investment, Total_in_stock, all_current_machines_data,transaction_data,Surplus = Make_a_report(machine,transaction,Owner,Month,Year)
            # purchased_data = serializers.serialize( "python", purchased_machines )
            context = {
                'Owner':Owner,
                'Month':Month,
                'Year':Year,
                'all_Profit':all_Profit,
                'all_Investment':all_Investment,
                'current_Profit':current_Profit,
                'current_Investment':current_Investment,
                'Total_in_stock':Total_in_stock,
                'all_current_machines_data':all_current_machines_data,
                'transaction_data':transaction_data,
                'machine_fields':machine_fields,
                'transaction_fields':transaction_fields,
                'Surplus':Surplus
            }
            return render(request, 'report.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = report_request_Form()

    return render(request, 'report_request.html', {'form': form})

# Create your views here.
