from django.contrib import admin

from transactions.models import Sale

# Register your models here.


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'wallet_to',
        'timestamp',
        'price_sale',
        'quantity',
        'transaction_id'
    )
    list_filter = (
        'wallet_to',
        'timestamp',
        'price_sale',
        'quantity',
        'transaction_id'
    )


admin.site.register(Sale, SaleAdmin)
