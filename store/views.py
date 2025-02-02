from django.shortcuts import render
from store.models import Customer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
    queryset = Customer.objects.all()

    return render(request, "index.html", { 'customers':list(queryset)})

@api_view()
def product_list(request):
    return Response('Ok')

@api_view()
def product_detail(request, id):
    return Response(id)