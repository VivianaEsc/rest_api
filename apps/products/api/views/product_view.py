from rest_framework import generics
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.products_serializers import ProductSerializer

class ProductListAPIVIew(GeneralListApiView):
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer    
