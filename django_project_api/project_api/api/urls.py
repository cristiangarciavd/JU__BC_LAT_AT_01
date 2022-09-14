from django.urls import path
from api.rest_api.rest_api import RestApi

urlpatterns = [
	path('products/<str:prod_name>', RestApi.get_products, name="products")
]