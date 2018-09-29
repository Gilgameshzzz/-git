# Filename  : forms.py 表单验证
# Date  : 2018/9/26
from django import forms

from users.models import User


class UserForm(forms.Form):
	username = forms.CharField(
		required=True,
		error_messages={'required': '账号必填'}
	)
	password = forms.CharField(
		required=True,
		error_messages={'required': '密码必填'}
	)

	def clean(self):
		# 		验证用户名是否存在
		user = User.objects.filter(username=self.cleaned_data.get('username'))
		if not user:
			raise forms.ValidationError({'username': '用户名不存在，请注册'})
		return self.cleaned_data


class UserRegisterForm(forms.Form):
	username = forms.CharField(
		required=True, max_length=20, min_length=5,
		error_messages={'required': '用户名必填', 'max_length': '用户名长度不能超过20个字符',
		                'min_length': '用户名长度不能少于5位'}
	)
	password = forms.CharField(
		required=True, max_length=20, min_length=8,
		error_messages={'required': '密码必填', 'max_length': '密码长度不能超过20个字符',
		                'min_length': '密码长度不能少于5位'}
	)
	password2 = forms.CharField(
		required=True, max_length=20, min_length=8,
		error_messages={'required': '确认密码必填', 'max_length': '密码长度不能超过20个字符',
		                'min_length': '密码长度不能少于5位'}
	)
	email = forms.EmailField(
		required=True,
		error_messages={'required': '邮箱必填'}
	)
	allow = forms.BooleanField(
		required=True,
	    error_messages={'required': '请同意用户协议'}
	)


	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		# 校验用户名是否存在
		user = User.objects.filter(username=username)
		if user:
			raise forms.ValidationError({'username': '用户名已存在'})
		if password2 != password:
			raise forms.ValidationError({'password2': '两次密码不一致'})
		return self.cleaned_data