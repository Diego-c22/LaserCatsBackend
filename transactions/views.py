from rest_framework import viewsets
from typing import List

from transactions.models import Sale
from transactions.serializers import SaleSerializer

# Create your views here.

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    http_method_names: List[str] = ['get', 'post']