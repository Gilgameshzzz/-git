from django.shortcuts import render

# Create your views here.
from goods.models import Goods


def goods_detail(request, id):
	if request.method == "GET":
		# 获取某个商品对象
		goods = Goods.objects.filter(pk=id).first()
		return render(request, 'detail.html', {'goods': goods})