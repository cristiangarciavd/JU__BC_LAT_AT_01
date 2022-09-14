from django.urls import path
from .views import Product

urlpatterns = [
	path('product/<str:prod_name>', Product.as_view())

]