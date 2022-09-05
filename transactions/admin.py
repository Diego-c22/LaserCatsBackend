from datetime import datetime
from django.contrib import admin
from django.utils.safestring import mark_safe

from transactions.models import Sale

# Register your models here.


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'wallet',
        'transaction_date',
        'price_sale',
        'quantity',
        'hash',
        'go_to_etherscan'
    )
    list_filter = (
        'wallet_to',
        'price_sale',
        'quantity',
        'transaction_id'
    )

    def wallet(self, obj):
        return f'{obj.wallet_to[:6]}...{obj.wallet_to[-6:]}'

    def hash(self, obj):
        return f'{obj.transaction_id[:6]}...{obj.transaction_id[-6:]}'

    def transaction_date(self, obj):
        return datetime.fromtimestamp(obj.timestamp)

    def go_to_etherscan(self, obj):
        return mark_safe(
            f'<a href="https://etherscan.io/tx/{obj.transaction_id}" style="background-color: #1d6aa7; padding: 5px 25px; border-radius: 4px; color: white; " >EtherScan</a>'
        )


admin.site.register(Sale, SaleAdmin)
