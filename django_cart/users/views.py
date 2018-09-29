from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from goods.models import GoodsCategory, Goods
from users.forms import UserForm, UserRegisterForm
from users.models import User


def index(request):
	if request.method == 'GET':
		# 获取商品的分类
		category_types = GoodsCategory.CATEGORY_TYPE
		# 获取商品，按照id教育排列
		goods = Goods.objects.all().order_by('category')
		# 循环商品分类，并组装结果
		data_all = {}
		for type1 in category_types:
			data = []
			count = 0
			for good in goods:
				# 计数count,大于4不在添加数据
				if count < 4:
					if type1[0] == good.category.category_type:
						data.append(good)
						count += 1
			data_all['goods_'+str(type1[0])] = data
		return render(request, 'index.html', {'data_all': data_all, 'category_types': category_types})


def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	if request.method == 'POST':
		# 1、表单验证
		form = UserForm(request.POST)
		# 使用is_vaild（）进行表单验证
		if form.is_valid():
			# form表单验证成功
			user = User.objects.filter(
				username=form.cleaned_data['username'],

				).first()
			# 	校验密码是否正确
			if not check_password(form.cleaned_data['password'], user.password):
				return HttpResponseRedirect(reverse('users:login'))
			else:
				# 添加登录成功的验证
				request.session['user_id'] = user.id
				return HttpResponseRedirect(reverse('users:index'))
		# 2、auth 模块验证
		# 3、auth。login登录
		else:
			# form验证失败，
			return render(request, 'login.html', {'form': form})


def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')

	if request.method == 'POST':
		# 校验参数
		form = UserRegisterForm(request.POST)
		# 判断is_valid()是否为True
		if form.is_valid():
			# 注册,使用make_password 进行密码加密，否则为明文
			data = form.cleaned_data
			username = data['username']
			data['password'] = make_password(data['password'])
			User.objects.create(username=username, password=data['password'], email=data['email'])
			# 跳转到登录界面
			return HttpResponseRedirect(reverse('users:login'))
		else:
			return render(request, 'register.html', {'form': form})


def base(request):
	if request.method == 'GET':
		user_id = request.session.get('user_id')
		if user_id:
			user = User.objects.get(pk=user_id)
	return JsonResponse({'user': user})

