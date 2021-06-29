from django.db.models import fields
from rest_framework import serializers
from .models import (product, categories, order, order_details)


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'

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