from django.db import models
from django import forms
import os 
import sys
from pathlib import Path
from djmoney.models.fields import MoneyField  

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Path(BASE_DIR).parent.absolute())
from config import *

CHOICES = [('سحب','سحب'),('ايداع','ايداع')]
class transaction(models.Model):
    Owner = models.CharField("المالك",max_length=15, choices=Owners, default=None)
    Date = models.DateField("التاريخ",blank=True,null=True)
    Amount = MoneyField("المبلغ",max_digits=14, decimal_places=2, default_currency='EGP',blank=True,null=True)
    Operation = models.CharField("نوع العملية",max_length=15, choices=CHOICES, default=None)

    def __str__(self):
        return self.Owner
# Create your models here.
