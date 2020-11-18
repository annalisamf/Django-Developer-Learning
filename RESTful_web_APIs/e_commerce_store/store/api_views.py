from rest_framework.generics import ListAPIView

from store.models import Product
from store.serializers import ProductSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
