from rest_framework import serializers
from .models import Charges, Balance

class ChargesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Charges
        fields= ['id', 'region', 'amount_per_month']

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Balance
        fields= ['id', 'amount', 'date']