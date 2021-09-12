from django.urls import path
from .views import *

urlpatterns = [
	path('<int:pk>', DetailProduct.as_view(), name="detail"),
	path('add/<int:product_id>', add_to_cart, name="addtocart"),
	path('cart/', add_to_cart, name="cart"),
]
