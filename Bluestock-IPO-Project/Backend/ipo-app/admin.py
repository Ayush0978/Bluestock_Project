from django.contrib import admin
from .models import IPO

# Register the IPO model so it shows up in the Django admin
@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'price_band', 'ipo_price', 'listing_price', 'listing_gain', 'cmp', 'current_return')
    search_fields = ('company_name',)
    list_filter = ('status', 'open_date', 'close_date')
