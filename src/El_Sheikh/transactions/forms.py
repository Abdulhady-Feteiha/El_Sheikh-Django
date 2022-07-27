from django import forms
from .models import Item
from djmoney.models.fields import MoneyField
import os
import sys

from config import *
class TransactionForm(forms.ModelForm):
    # Machine_TYPE = forms.ChoiceField(choices=Machine_types)
    # Location = forms.ChoiceField(choices=Locations)
    # Mark = forms.ChoiceField(choices=Marks)
    # Features = forms.CharField(max_length=100,widget=forms.Textarea())
    # Owner = forms.ChoiceField(choices=Owners)
    # sold = forms.BooleanField(required=False)
    # purchase_date = forms.DateField()
    # purchase_price = MoneyField(max_digits=14, decimal_places=2)
    # sell_date = forms.DateField()
    # sell_price = MoneyField(max_digits=14, decimal_places=2)
    # def clean(self):
    #     cleaned_data = super(TransactionForm, self).clean()
    #     Machine_TYPE = cleaned_data.get('Machine_TYPE')
    #     Location = cleaned_data.get('Location')
    #     Mark = cleaned_data.get('Mark')
    #     Owner = cleaned_data.get('Owner')
    #     sold = cleaned_data.get('sold')
    #     if not Machine_TYPE and not Location and not Mark and not Owner:
    #         raise forms.ValidationError('You have to write something!')
    class Meta:
        model = Item
        fields = ['Machine_TYPE','Location','Mark','Features','Sold']
    