from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
	cat_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=150)
	description = models.CharField(max_length=250)
	def __str__(self):
		return self.name


class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=150)
	price = models.DecimalField(blank=True, decimal_places=2, max_digits=50)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to="images/")
	cat = models.ForeignKey(Category, on_delete=models.CASCADE)
	def __str__(self):
		return self.name


class Cart(models.Model):
	cart_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateField(auto_now=True)


class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	price = models.DecimalField(blank=True, decimal_places=2, max_digits=50)
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
