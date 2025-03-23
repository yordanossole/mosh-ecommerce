from django.shortcuts import render
from store.models import Customer
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    queryset = Customer.objects.all()

    return render(request, "index.html", { 'customers':list(queryset)})

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method =='GET':
        queryset = Product.objects.select_related('colloection').all()
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.validated_data
        #     return Response('OK')
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.is_valid(raise_exception=True) # Instead of the above if else statement - It automaticaly sends response with status code if there is error
        # serializer.validated_data # To access validated data
        serializer.save() # To save the data back to database using save methods of ModelSerializers
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id):
    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     # return Response(status=404)
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    # another way to do the same thing as above
    # product = get_object_or_404(Product, pk=id)
    # serializer = ProductSerializer(product)
    # return Response(serializer.data)

    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if product.orderitems.count() > 0:
            return Response({'error': "Product can't be deleted because it has ordered items."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view()
def collection_detail(request, pk):
    return Response('Ok')