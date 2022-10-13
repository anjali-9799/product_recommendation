# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


class ProductListApiView(APIView):

    def get(self, request, *args, **kwargs):
        '''
        Just to check the posted data
        '''
        product = Product.objects.filter()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'product_name': request.data.get('product_name'),
            'categories': request.data.get('categories'),
            'description': request.data.get('description'),
            'unit_price': request.data.get('unit_price'),
            'quantity': request.data.get('quantity'),
            'for_sale': request.data.get('for_sale'),
            'in_stock': request.data.get('in_stock'),
            'rating': request.data.get('rating'),
            'review': request.data.get('review'),
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
