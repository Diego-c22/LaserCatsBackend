from rest_framework.serializers import ModelSerializer

from transactions.models import Sale

class SaleSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = ('wallet_to', 'timestamp', 'transaction_id', 'price_sale', 'quantity')