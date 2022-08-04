from django.db import models
from django import forms
import os 
import sys
from pathlib import Path
from djmoney.models.fields import MoneyField  
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Path(BASE_DIR).parent.absolute())
from config import *

class report_request(models.Model):
    Owner = models.CharField(max_length=15, choices=Owners, default=None)
    Month = models.IntegerField(default=None,validators=[MaxValueValidator(12), MinValueValidator(1)])
    Year = models.IntegerField(default=None,validators=[MaxValueValidator(date.today().year), MinValueValidator(2021)])
    # Owner = MultiSelectField(choices=Owners)
    def __str__(self):
        return self.Owner

class report(models.Model):
    Owner = models.CharField(verbose_name="المالك",max_length=15, choices=Owners, default=None)
    Month = models.IntegerField(verbose_name="شهر",default=None,validators=[MaxValueValidator(12), MinValueValidator(1)])
    Year = models.IntegerField(verbose_name="ستة",default=None,validators=[MaxValueValidator(date.today().year), MinValueValidator(2021)])

    def __str__(self):
        return self.Owner
# Create your models here.

# Create your models here.
