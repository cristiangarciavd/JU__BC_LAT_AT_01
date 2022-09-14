from django.shortcuts import render
from django.views import View
<<<<<<< Updated upstream
from .models import Product, Search
from datetime import date
=======
from .db_manager.db_manager import DbManager
from django.http import JsonResponse
>>>>>>> Stashed changes
# Create your views here. 
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

<<<<<<< Updated upstream


def get_products_by_search(request, search_term):
	objects = Product.objects.filter(search=search_term)
	list_of_objects=[]
	for one_object in objects:
		list_of_objects.append(one_object)
	return list_of_objects


def create_search(search_term): #It also updates the search
	try:
		search = Search.object.get(name=search_term)
		search.updated_at = date.today()
		search.times_searched =search.times_searched + 1
		search.save()
	except DoesNotExist:
		search = Search(name=search_term, created_at=date.today(), updated_at=date.today())
		search.save()

def create_product(dict_product, search_term): #product is the dict where it has the information
	product_name = dict_product["product"]
	product_price = dict_product["price"]
	product_img = dict_product["link_img"]
	product_url  = dict_product["link_url"]
	product_origin = dict_product["origin"]

	new_product = Product(name=product_name, 
						price=product_price, 
						image_url=product_img,
						url=product_url,
						search=search_term,
						origin=product_origin)
	new_product.save()


def get_most_popular():
	list_of_popular_products = []
	popular_searchs = Search.object.order_by('times_searched')[:5]
	for search in popular_searchs:
		list_products = get_products_by_search(search)
		list_of_popular_products.append(list_products)
	return list_of_popular_products
=======
products_mesa_mock = [
	{"name":"mesa marron","price":3,"image_url":"sdsds","url":"sadasd"},
	{"name":"mesa azul","price":3,"image_url":"sdsds","url":"sadasd"},
	{"name":"mesa amarilla","price":3,"image_url":"sdsds","url":"sadasd"}
	]

products_mouse_mock = [
	{"name":"mouse marron","price":3,"image_url":"sdsds","url":"sadasd"},
	{"name":"mouse azul","price":3,"image_url":"sdsds","url":"sadasd"},
	{"name":"mouse amarilla","price":3,"image_url":"sdsds","url":"sadasd"}
	]

def parser(item):
	if item == 'mouse':
		product = products_mouse_mock
	else:
		product = products_mesa_mock
	return product


class CRUDView(View):

	###Find Products by Search Term
	def get(self, request, search_term):
		db_manager = DbManager()
		search = db_manager.find_term(search_term)
		if search:
			search = db_manager.term_up_today(search)
			if search:
				data = db_manager.find_products(search)
			else:
				db_manager.delete_search(search_term)
				db_manager.create(parser(search_term),search_term)
		else:
			db_manager.create(parser(search_term),search_term)
			data = parser(search_term)
		return JsonResponse(data, safe = False)
		

	####Delete search term and products
	# def get(self, request, search_term):
	# 	db_manager = DbManager()
	# 	data = db_manager.delete_search(search_term)
	# 	return JsonResponse(data)


	####Create Products and Search Term
	# def get(self, request, search_term):
	# 	db_manager = DbManager()
	# 	
	# 	db_manager.create([{"name":"mesa marron","price":3,"image_url":"sdsds","url":"sadasd"},{"name":"mesa azul","price":3,"image_url":"sdsds","url":"sadasd"},{"name":"mesa amarilla","price":3,"image_url":"sdsds","url":"sadasd"}], search_term)
>>>>>>> Stashed changes
