from rest_framework import routers

from transactions.views import SaleViewSet

route = routers.SimpleRouter()

route.register('transactions', SaleViewSet)

urlpatterns = route.urls