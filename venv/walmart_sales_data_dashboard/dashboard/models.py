from django.db import models
from datetime import date

# Create your models here.
from django.forms import forms




class Sales2_Sales_Measures_by_Period(models.Model):
    prime_item_nbr = models.PositiveIntegerField(),
    prime_item_dec = models.CharField(max_length=150),
    id = models.PositiveIntegerField(primary_key=True, editable=False),
    upc = models.PositiveIntegerField(),
    wm_week = models.PositiveIntegerField(editable=False),
    wm_month = models.DateField(),
    fiscal_wm_quarter = models.DateField(),
    fiscal_wm_year = models.DateField(),
    pos_qty = models.PositiveIntegerField(),
    pos_sales = models.DecimalField(max_digits=10, decimal_places=2),