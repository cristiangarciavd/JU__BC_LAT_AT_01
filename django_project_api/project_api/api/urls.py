from django.urls import path
from .views import CRUDView

urlpatterns=[
    path('products/', CRUDView.as_view(), name="products_list"),
    path('products/<str:search_term>', CRUDView.as_view(), name="products_process"),
]