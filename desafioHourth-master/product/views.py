from django.shortcuts import render
from .models import Product

import requests
import json
from django.db.models.aggregates import Sum
from rest_framework import viewsets
from .serializers import ProductSerializer
import time

class GetProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.values('product_url_image', 'product_url', 'product_url_created_at').annotate(
            total_sales=Sum('vendas_no_dia'))
        return queryset


API = 'https://mc3nt37jj5.execute-api.sa-east-1.amazonaws.com/default/hourth_desafio'

dict = []

def list_products(request):
    response = requests.get(API)

    retur = json.loads(response.content)

    for obj in retur:
        Product.objects.get_or_create(product_url_image=obj['product_url__image'], product_url=obj['product_url'],
                                      product_url_created_at=obj['product_url__created_at'],
                                      vendas_no_dia=int(obj['vendas_no_dia']),
                                      consult_date=obj['consult_date'])

        if [obj['product_url']] == [obj['product_url']]:
            dict = [obj['product_url'], obj['consult_date']]
            print(dict)

    prod = Product.objects.values('product_url').annotate(total_sales=Sum('vendas_no_dia'))

    context = {
        'products': prod
    }

    return render(request, 'index.html', {'context': context})
