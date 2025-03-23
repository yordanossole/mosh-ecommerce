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

class ProductSerializer(serializers.ModelSerializer):
    # inventory = serializers.IntegerField(write_only=True) # Deserialize only, not included in response
    # inventory = serializers.IntegerField(read_only=True)  # Serialize only, not accepted as input

    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'inventory', 'price_with_tax', 'colloection']
        # extra_kwargs = {
        #     'inventory': {'write_only': True} # Deserialize only, not included in response
        # }
        # extra_kwargs = {
        #     'inventory': {'read_only': True}  # Serialize only, not accepted as input
        # }
        
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product : Product):
        return product.unit_price * Decimal(1.1)
    
    # overiding validate() method - which would be called when "validated_data" accessed (for custom validation) 
    # def validate(self, data):
    #     if data['password'] != data['confirm_password']:
    #         return serializers.ValidationError('Passwords do not match')
    #     return data

    # The save method invoked to save the object in the view calls one of this methods depending of the validated_data 
    # # Overide create and update methods to handle saving and updating models by our own
    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product

    # def update(self, instance, validated_data):
    #     instance.unit_price = validated_data.get('unit_price')
    #     instance.save()
    #     return instance