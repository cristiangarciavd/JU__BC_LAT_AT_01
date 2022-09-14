from django.shortcuts import render
from django.views import View
from .models import Product, Search
from datetime import date
# Create your views here. 
class CRUDView(View):
	pass


# def get_products_by_search(request, search_term):
# 	objects = Product.objects.filter(search=search_term)
# 	list_of_objects=[]
# 	for one_object in objects:
# 		list_of_objects.append(one_object)
# 	return list_of_objects


# def create_search(search_term): #It also updates the search
# 	try:
# 		search = Search.object.get(name=search_term)
# 		search.updated_at = date.today()
# 		search.times_searched =search.times_searched + 1
# 		search.save()
# 	except DoesNotExist:
# 		search = Search(name=search_term, created_at=date.today(), updated_at=date.today())
# 		search.save()

# def create_product(dict_product, search_term): #product is the dict where it has the information
# 	product_name = dict_product["product"]
# 	product_price = dict_product["price"]
# 	product_img = dict_product["link_img"]
# 	product_url  = dict_product["link_url"]
# 	product_origin = dict_product["origin"]

# 	new_product = Product(name=product_name, 
# 						price=product_price, 
# 						image_url=product_img,
# 						url=product_url,
# 						search=search_term,
# 						origin=product_origin)
# 	new_product.save()


# def get_most_popular():
# 	list_of_popular_products = []
# 	popular_searchs = Search.object.order_by('times_searched')[:5]
# 	for search in popular_searchs:
# 		list_products = get_products_by_search(search)
# 		list_of_popular_products.append(list_products)
# 	return list_of_popular_products