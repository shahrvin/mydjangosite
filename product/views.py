from django.views.generic import ListView , DetailView

from product.models import Product


class Home(ListView):
	queryset = Product.objects.all()[:12]
	template_name = "index.html"

class DetailProduct(DetailView):
	model = Product
	template_name = "detail.html"
