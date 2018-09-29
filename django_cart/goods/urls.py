# Filename  : urls.py
# Date  : 2018/9/27
from django.conf.urls import url

from goods import views

urlpatterns = [
	# 	商品详情
	url(r'^goods_detail/(\d+)/', views.goods_detail, name='goods_detail')

]