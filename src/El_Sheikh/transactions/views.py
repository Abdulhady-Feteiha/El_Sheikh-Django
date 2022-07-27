from django.shortcuts import render
from .forms import TransactionForm


def Transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()  
    else:
        form = TransactionForm()

    return render(request, 'transaction.html', {'form': form})
# Create your views here.
