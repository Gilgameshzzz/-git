# Filename  : choose_data.py
# Date  : 2018/11/17

import random

import pandas as pd

data = pd.read_csv('house.csv')

postion = data['经纬度'].tolist()

lat = []
lon = []

for i in postion:
	a, b = i.split(',')
	a = float(a)
	b = float(b)
	lat.append(a)
	lon.append(b)

latitude = pd.DataFrame(lat, columns=['latitude'])
longitude = pd.DataFrame(lon, columns=['longitude'])
lat_lon = pd.concat([data, latitude, longitude], axis=1)

lat_lon.to_csv('new_data.csv', sep=',', index=None)

if __name__ == '__main__':
	# print(latitude)
	# print(longitude)
	print('ok')