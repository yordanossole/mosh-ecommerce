from django.shortcuts import render
from store.models import Customer

# Create your views here.
def index(request):
    queryset = Customer.objects.all()

    return render(request, "index.html", { 'customers':list(queryset)})