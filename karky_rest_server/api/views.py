from django.http.response import JsonResponse
from django.shortcuts import render
from products.models import Product
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
# objects.filter(Q(filed_nam1__icontains=search_query) | Q(filed_name2__icontains=search_query))

from api.serializers import ProductSerializer


# Create your views here.
def no_rest_no_model(request, *args, **kwargs):
    guests = [{'id': 1, 'username': 'xxx'}, {'id': 2, 'username': 'yyy'}]
    return JsonResponse(guests, safe=False)


def no_rest_from_model(request, *args, **kwargs):
    data = Product.objects.all()
    response = {'products': list(data.values())}
    return JsonResponse(response, safe=False)


@api_view(['GET', 'POST'])
def FBV_list(request, *args, **kwargs):
    if request.method == 'GET':
        products = Product.objects.filter(product_id=request.query_params.get('product_id'))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
