from django.urls import path
from . import views

urlpatterns = [
     path('',views.Receiver.get_products, name = 'products')
]