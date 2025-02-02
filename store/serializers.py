from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source = 'unit_price') # changing the name in the response
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # 1.1
    # colloection = serializers.PrimaryKeyRelatedField(
    #     queryset = Collection.objects.all()
    # )
    # 1.2
    # colloection = serializers.StringRelatedField()

    # 2
    colloection = CollectionSerializer()
    # 3
    colloection = serializers.HyperlinkedRelatedField(
        queryset = Collection.objects.all(),
        view_name = 'collection-detail'
    )

    def calculate_tax(self, product : Product):
        return product.unit_price * Decimal(1.1)