import os 
import sys
from pathlib import Path
from django.db import models
from djmoney.models.fields import MoneyField  
from multiselectfield import MultiSelectField

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Path(BASE_DIR).parent.absolute())
from config import *

class machine(models.Model):
  Machine_TYPE = models.CharField("الماكينة",max_length=15, choices=Machine_types, default='منشار')
  Location = models.CharField("المخزن",max_length=15, choices=Locations, default='فهمي')
  Mark = models.CharField("الماركة",max_length=15, choices=Marks, default='بلدي')
  Features = models.TextField("خصائص",default=None,null=True,blank=True)
  Owners = MultiSelectField("المالك",choices=Owners)
  purchase_date = models.DateField("تاريخ الشراء",blank=True,null=True)
  purchase_price = models.IntegerField("سعر الشراء",blank=True,null=True)
  sell_date = models.DateField("تاريخ البيع",blank=True,null=True)
  sell_price = models.IntegerField("سعر البيع",blank=True,null=True)

  def __str__(self):
    return self.Machine_TYPE
# Create your models here.