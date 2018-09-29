# Filename  : functions.py
# Date  : 2018/9/28
from datetime import datetime
import random


def get_order_sn():
	sn = ''
	s = '1234567890qwertyuiopasdfghjklzxcvbnm'
	for i in range(10):
		sn += random.choice(s)
	sn += datetime.now().strftime('%Y%m%d%H%M%S')
	return sn