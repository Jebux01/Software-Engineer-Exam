from django.core.checks import messages
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import product, categories
from .serializers import productSerializer, categorieSerializer


@api_view(['POST'])
def productCreate(request):
    serializer = productSerializer(data=request.data)
    if (serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def productDetail(request, pk):
    productDet = product.objects.get(id=pk)
    serializer = productSerializer(productDet, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def categorieCreate(request):
    serializer = categorieSerializer(data=request.data)
    if (serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def productUpdate(request, pk):
    productUp = product.objects.get(id=pk)
    serializer = productSerializer(instance=productUp, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def productDelete(request, pk):
    productDel = product.objects.get(id=pk)
    productDel.delete()
    return Response("Se elimino el producto correctamente", status=status.HTTP_200_OK)

@api_view(['GET'])
def validateStock(request, pk):
    prod = product.objects.get(id=pk)
    serializer = productSerializer(prod, many=False)
    if (serializer.data['stock'] > 0):
        return Response({"data": 1}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Producto sin stock"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)