from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Product, Search
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from api.rest_api.rest_api import RestApi


# Create your views here.


def get_products_by_search(request, search_term):
    objects = Product.objects.filter(search=search_term)
    list_of_objects = []
    for one_object in objects:
        list_of_objects.append(one_object)
    return list_of_objects


# def create_search(request, search_term):
#	try:
#		search = Search.object.get(name=search_term)
#		search.updated_at = date.today()
#		search.save()
#	except DoesNotExist:
#		search = Search(name=search_term, created_at=date.today(), updated_at=date.today())
#		search.save()

def create_product(request, dict_product, search_term):  # product is the dict where it has the information
    product_name = dict_product["product"]
    product_price = dict_product["price"]
    product_img = dict_product["link_img"]
    product_url = dict_product["link_url"]
    product_origin = dict_product["origin"]

    new_product = Product(name=product_name,
                          price=product_price,
                          image_url=product_img,
                          url=product_url,
                          search=search_term,
                          origin=product_origin)
    new_product.save()


class Product(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, requests, prod_name):
        restapi = RestApi()
        product = restapi.get_products(prod_name)
        return JsonResponse(product, safe=False)
