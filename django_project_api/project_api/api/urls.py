from django.urls import path
from .views import CRUDView

urlpatterns=[
	path('popular/', CRUDView.as_view(), name='CRUDView')
]