# Filename  : urls.py
# Date  : 2018/9/27
from django.conf.urls import url

from orders import views

urlpatterns = [
	# 	下单
	url(r'^order/', views.order, name='order'),

]