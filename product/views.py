from django.views.generic import ListView

from product.models import Product


class Home(ListView):
	queryset = Product.objects.all()[:12]
	template_name = "index.html"