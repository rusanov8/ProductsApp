from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

    @staticmethod
    def validate_title(value):
        if len(value) == 0:
            raise serializers.ValidationError('Наименование товара не может быть пустым.')
        return value

    @staticmethod
    def validate_price(value):
        if value <= 0:
            raise serializers.ValidationError('Цена должна быть положительным числом.')
        return value

