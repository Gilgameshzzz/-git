# Filename  : urls.py
# Date  : 2018/9/27
from django.conf.urls import url

from cart import views

urlpatterns = [
	url(r'add_cart/', views.add_cart, name='add_cart'),
	# 	刷新价格
	url(r'^f_price/', views.f_price, name='f_price'),
	# 购物车
	url(r'^cart/', views.cart, name='cart'),

]