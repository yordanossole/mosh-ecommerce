from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection

# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
#     # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
#     price = serializers.DecimalField(max_digits=6, decimal_places=2, source = 'unit_price') # changing the name in the response
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     # 1
#     # colloection = serializers.PrimaryKeyRelatedField(
#     #     queryset = Collection.objects.all()
#     # )
#     # 2
#     # colloection = serializers.StringRelatedField()

#     # 3
#     # colloection = CollectionSerializer()
#     # 4
#     colloection = serializers.HyperlinkedRelatedField(
#         queryset = Collection.objects.all(),
#         view_name = 'collection-detail'
#     )

#     def calculate_tax(self, product : Product):
#         return product.unit_price * Decimal(1.1)

# using ModelSerializer class instead of Serializer
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']
        # fields = '__all__' # to serialize all fields of the model

class ProductSerializer(serializers .ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'colloection']
        
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product : Product):
        return product.unit_price * Decimal(1.1)
    
    # overiding validate() method
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Passwords do not match')
    #     return data