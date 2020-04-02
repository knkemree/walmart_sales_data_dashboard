from django.contrib import admin
from .models import Sales2_Sales_Measures_by_Period
# Register your models here.



class Sales2_Sales_Measures_by_PeriodAdmin(admin.ModelAdmin):
    list_display = ('prime_item_dec', 'wm_week', 'wm_month', 'pos_qty', 'pos_sales')
    
admin.site.register(Sales2_Sales_Measures_by_Period, Sales2_Sales_Measures_by_PeriodAdmin)
