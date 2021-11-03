from django.urls import path
from .views import ChargeView, BalanceView

urlpatterns = [  
    path('charges', ChargeView.as_view(), name='charges'),
    path('balance', BalanceView.as_view(), name='balance'),
]