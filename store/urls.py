from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index),
    path('products/', views.product_list),
    # path('products/<id>', views.product_detail)
    path('products/<int:id>', views.product_detail)
]