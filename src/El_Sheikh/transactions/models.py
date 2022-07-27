from django.db import models
from djmoney.models.fields import MoneyField
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR,'src/El_Sheikh/'))
from config import *

class Item(models.Model):
  Machine_TYPE = models.CharField(max_length=15, choices=Machine_types, default='منشار')
  Location = models.CharField(max_length=15, choices=Locations, default='فهمي')
  Mark = models.CharField(max_length=15, choices=Marks, default='بلدي')
  Features = models.TextField(default="آدخل آي خصائص اضافية")
  Owner = models.CharField(max_length=15, choices=Owners, default='ماما')
  Sold = models.BooleanField(default=False)
#   purchase_date = models.DateField()
#   purchase_price = MoneyField(max_digits=14, decimal_places=2, default_currency='EGP')
#   sell_date = models.DateField()
#   sell_price = MoneyField(max_digits=14, decimal_places=2, default_currency='EGP')
  def __str__(self):
    return self.Machine_TYPE
  
# Create your models here.

