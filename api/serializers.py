from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import (product, categories, order, order_details, status)


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'

class productStockSerializer(serializers.ModelSerializer):
    class Meta:
        Model = product
        fields = ('stock')

class categorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = categories
        fields = '__all__'

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'


class orderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_details
        fields = '__all__'

class statuSerializer(serializers.ModelSerializer):
    class Meta:
        model = status
        fields = '__all__'