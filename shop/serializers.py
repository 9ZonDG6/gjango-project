from rest_framework import serializers
from shop import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

    def validate(self, attrs: dict):
        if attrs['price'] < 0:
            raise serializers.ValidationError('Цена ниже нуля')

        return attrs
