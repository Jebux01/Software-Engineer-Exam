from enum import Flag
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import statuSerializer, orderSerializer, productSerializer, orderDetailSerializer
from .models import product
from rest_framework.parsers import JSONParser
import functools
import operator


@api_view(['POST'])
def statusCreated(request):
    serializer = statuSerializer(data=request.data)
    if (serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def orderCreated(request):
    dataRec = JSONParser().parse(request)
    products = list(map(lambda item: productSerializer(product.objects.filter(
        id=item['id']), many=True).data, dataRec['details']))
    totals = list(map(float,list(map(lambda prod: (float(prod[0]['price']) * list(filter(lambda x: x['id'] == prod[0]['id'], dataRec['details']))[0]['quantity']), products))))
    dataOrder = {
        "total": sum(totals),
        "user": dataRec['user']
    }

    serializerOrder = orderSerializer(data=dataOrder)
    if (serializerOrder.is_valid()):
        serializerOrder.save()
        idOrder = serializerOrder.data['id']
        details = list(map(lambda prod: {"id_order": idOrder, "codProd": prod[0]['id'], "quantity": list(filter(
            lambda x: x['id'] == prod[0]['id'], dataRec['details']))[0]['quantity'], "priceProd": prod[0]['price']}, products))
        
        saveDetails = list(map(saveOrderDetails, details))
        print(saveDetails)

    else:
        return Response(serializerOrder.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # oDetails = []
    # outStock = []
    # oPending = []
    # for index in range(len(products)):
    #     res = validateStock(
    #         products[index][0]['stock'], data['details'][index]['quantity'])

    #     if (res['stock'] and res['quantityMissing'] > 0):
    #         products[index][0]['quantityMissing'] = res['quantityMissing']
    #         oPending.append(products[index][0])
    #     elif (res['stock']):
    #         products[index][0]['stockNew'] = res['stockNew']
    #         oDetails.append(products[index][0])
    #     else:
    #         outStock.append(products[index][0])

    return Response(dataOrder, status=status.HTTP_201_CREATED)


def saveOrderDetails(produc):
    serializerDetails = orderDetailSerializer(data=produc)
    if (serializerDetails.is_valid()):
        serializerDetails.save()
        return serializerDetails.data
    else:
        return serializerDetails.error


@api_view(['GET'])
def validateStock(request, pk):
    prod = product.objects.get(id=pk)
    serializer = productSerializer(prod, many=False)
    if (serializer.data['stock'] > 0):
        return Response({"data": 1}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Producto sin stock"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
