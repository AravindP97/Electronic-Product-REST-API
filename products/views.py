from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http.response import HttpResponse

from .models import Producttable, Laptoptable, Mobiletable
from .serializers import ProducttableSerializer
from .decorators import verify_user


class productsView(APIView):
    serializer_class = ProducttableSerializer

    def get(self, request, format=None):
        user = verify_user(request)
        if user is None:
            response_data = {
                'Message': 'Permission denied Unauthenticated!',
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        data = Producttable.objects.all()
        serializer = self.serializer_class(data, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        user = verify_user(request)
        if user is None:
            response_data = {
                'Message': 'Permission denied Unauthenticated!',
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        product_serializer = ProducttableSerializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            response_data = {
                'Message': 'Product Created Successfully',
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class productUpdate(APIView):
    serializer_class = ProducttableSerializer

    def get(self, request, pk, format=None):
        user = verify_user(request)
        if user is None:
            response_data = {
                'Message': 'Permission denied Unauthenticated!',
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        try:
            product = Producttable.objects.get(pk=pk)
        except Producttable.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        serializer = ProducttableSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = verify_user(request)
        if user is None:
            response_data = {
                'Message': 'Permission denied Unauthenticated!',
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        try:
            product = Producttable.objects.get(pk=pk)
        except Producttable.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        serializer = ProducttableSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'Message': 'Product Updated Successfully',
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        user = verify_user(request)
        if user is None:
            response_data = {
                'Message': 'Permission denied Unauthenticated!',
            }
            return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
        try:
            product = Producttable.objects.get(pk=pk)
        except Producttable.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        product.delete()
        response_data = {
            'Message': 'Product Deleted Successfully',
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
