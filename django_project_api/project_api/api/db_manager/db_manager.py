from django.db import models
from api.models import Product

#from ..models import Product
class DBManager():

	def get_products_by_search(self, search_term):
		product_list = []
		product_object = models.Product.objects.filter(search=search_term)
		print(product_object)



