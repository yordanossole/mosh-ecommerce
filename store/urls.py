from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.index),
    path('products/', views.product_list),
    # path('products/<id>', views.product_detail)
    path('products/<int:id>', views.product_detail), # to make it only works for int id
    path('collections/<int:pk>', views.collection_detail, name='collection-detail')
]