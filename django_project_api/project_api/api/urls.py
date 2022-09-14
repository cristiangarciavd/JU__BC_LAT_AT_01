from django.urls import path
from . import views

urlpatterns=[
    path('products/', CRUDView.as_view(), name="products_list"),
    path('products/<str:search_term>', CRUDView.as_view(), name="products_process"),
]