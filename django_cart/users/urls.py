# Filename  : urls.py
# Date  : 2018/9/26
from django.conf.urls import url

from users import views

urlpatterns = [
	url(r'^index/', views.index, name='index'),
	url(r'^login/', views.login, name='login'),
	url(r'^register/', views.register, name='register'),
	url(r'^base/', views.base, name='base'),
]