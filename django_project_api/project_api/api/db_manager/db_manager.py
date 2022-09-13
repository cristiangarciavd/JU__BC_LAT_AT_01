from api.models import Product


class DBManager():

	def get_products_by_search(self, search_term):
		product_list = []
		product_object = Product()
		aux = models.product_object.objects.filter(search=search_term)
		print(aux)



