from .project_api.api.models import Product
#from ..models import Product


class DBManager():

	def get_products_by_search(self, search_term):
		product_list = []
		product_object = models.Product.objects.filter(search=search_term)
		return product_object


manager_object = DBManager()
aux = manager_object.get_products_by_search('Mouse Gamer')
print(aux)