from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Orders
from .serializers import OrderSerializer
from .serializers import OrderSerializerAll


class OrderListApiView(APIView):

    def get(self, request, *args, **kwargs):
        '''
        Just to check the posted data
        '''
        order = Orders.objects.filter()
        serializer = OrderSerializerAll(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'product': request.data.get('product'),
            'total_price': request.data.get('total_price'),
            'quantity': request.data.get('quantity'),
        }
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
