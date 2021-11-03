from django.shortcuts import render
from rest_framework import generics
from forecast.models import Charges, Balance
from .serializers import ChargesSerializer, BalanceSerializer

class ChargeView(generics.ListAPIView):
    serializer_class = ChargesSerializer
    queryset = Charges.objects.all()

class BalanceView(generics.ListAPIView):
    serializer_class = BalanceSerializer
    queryset = Balance.objects.all()
