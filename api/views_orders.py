from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import statuSerializer, orderSerializer, productSerializer
from .models import product
from rest_framework.parsers import JSONParser


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
    data = JSONParser().parse(request)
    products = list(map(lambda item: productSerializer(product.objects.filter(description=item['description']), many=True).data, data['details']))

    #comparar stock vs cantida a pedir, si el stock es 0 no se agrega, si el stock - la cantidad da negativo tampoco, solo se regresa el stock
    for i in products:
        print(i)
    # for req in data['details']:
    #     data = list(filter(lambda item: (item[0]['stock'] - req['quantity']) > 0, productsData))
    #     print(data)
    
    return Response(data, status=status.HTTP_201_CREATED)
