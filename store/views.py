# from django.shortcuts import render
# from store.models import Customer
# from .models import Product
# from .serializers import ProductSerializer
# from django.shortcuts import get_object_or_404

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# # Create your views here.
# def index(request):
#     queryset = Customer.objects.all()

#     return render(request, "index.html", { 'customers':list(queryset)})

# @api_view()
# def product_list(request):
#     queryset = Product.objects.select_related('colloection').all()
#     serializer = ProductSerializer(queryset, many=True, context={'request': request})
#     return Response(serializer.data)

# @api_view()
# def product_detail(request, id):
#     # try:
#     #     product = Product.objects.get(pk=id)
#     #     serializer = ProductSerializer(product)
#     #     return Response(serializer.data)
#     # except Product.DoesNotExist:
#     #     # return Response(status=404)
#     #     return Response(status=status.HTTP_404_NOT_FOUND)

#     # another way to do the same thing as above

#     product = get_object_or_404(Product, pk=id)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)

# @api_view()
# def collection_detail(request, pk):
#     return Response('Ok')