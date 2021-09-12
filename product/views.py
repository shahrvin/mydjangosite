from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from product.models import Product, Cart, CartItem


class Home(ListView):
    queryset = Product.objects.all()[:12]
    template_name = "index.html"


class DetailProduct(DetailView):
    model = Product
    template_name = "detail.html"


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if product:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cartitem, itemcreated = CartItem.objects.get_or_create(product=product, cart=cart, price=product.price)
        cartitem.quantity+=1
        cartitem.save()
        messages.success(request,"cart updated")
        return redirect('detail',product_id)

