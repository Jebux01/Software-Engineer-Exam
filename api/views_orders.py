from datetime import datetime
from enum import Flag
from django.shortcuts import render
from rest_framework import  status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import statuSerializer, orderSerializer, productSerializer, orderDetailSerializer
from .models import product, order, order_details, status as StatusOrder
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
    dataRec = JSONParser().parse(request)
    products = list(map(lambda item: productSerializer(product.objects.filter(id=item['prod']), many=True).data, dataRec['details']))
    print(products)
    totals = list(map(float, list(map(lambda prod: (float(prod[0]['price']) * list(filter(lambda x: x['prod'] == prod[0]['id'], dataRec['details']))[0]['quantity']), products))))
    dataOrder = {
        "total": sum(totals),
        "user": dataRec['user']
    }

    serializerOrder = orderSerializer(data=dataOrder)
    if (serializerOrder.is_valid()):
        serializerOrder.save()
        idOrder = serializerOrder.data['id']
        details = list(map(lambda prod: {"order": idOrder, "prod": prod[0]['id'], "quantity": list(filter(
            lambda x: x['prod'] == prod[0]['id'], dataRec['details']))[0]['quantity'], "priceProd": prod[0]['price']}, products))

        saveDetails = list(map(saveOrderDetails, details))
        error = list(filter(lambda x: x['error'] == True, saveDetails))

        if (len(error) > 0):
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": f"Orden creada correctamente con el numero {idOrder}"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializerOrder.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def saveOrderDetails(prod):
    serializerDetails = orderDetailSerializer(data=prod)
    if (serializerDetails.is_valid()):
        serializerDetails.save()
        return {"error": False}
    else:
        return {"error": True, "message": serializerDetails.errors}


@api_view(['GET'])
def orderFull(request, pk):
    header = order.objects.get(id=pk)
    serializer = orderSerializer(header, many=False)

    details = order_details.objects.filter(order_id=pk)
    serializerDet = orderDetailSerializer(details, many=True)

    detailsProd = []
    for prod in serializerDet.data:
        add = {}
        add.update(prod)
        add.update({"description": productSerializer(product.objects.get(id=prod['prod']), many=False).data['description']})
        detailsProd.append(add)

    enData = serializer.data
    enData.update({"details": detailsProd})
    
    return Response(enData, status=status.HTTP_200_OK)

@api_view(['GET'])
def orderStatus(request, pk):
    header = order.objects.filter(status_id=pk)
    serializer = orderSerializer(header, many=True)
    enData = serializer.data

    allOrders = []
    
    for orderAdd in enData:
        add = {}
        add.update(orderAdd)
        prods = orderDetailSerializer(order_details.objects.filter(order_id=orderAdd['id']), many=True).data
        prodsD = []
        for prod in prods:
            adD = {}
            adD.update(prod)
            adD.update({"description": productSerializer(product.objects.get(id=prod['prod']), many=False).data['description']})
            prodsD.append(adD)
        
        add.update({"details": prodsD})
        allOrders.append(add)
    
    return Response(allOrders, status=status.HTTP_200_OK)

@api_view(['PUT'])
def orderUpdate(request, pk):
    orderUp = order.objects.get(id=pk)
    request.data['dateInProcess'] = datetime.now()
    serializer = orderSerializer(instance=orderUp, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def orderDelete(request, pk):
    orderDel = order.objects.get(id=pk)
    orderDel.delete()
    return Response("Se elimino la orden correctamente", status=status.HTTP_200_OK)


@api_view(['GET'])
def statusGet(request):
    statusAll = StatusOrder.objects.all()
    serializer = statuSerializer(statusAll, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


