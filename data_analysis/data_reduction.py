# Filename  : data_reduction.py
# Date  : 2018/11/17
import json

import pandas as pd

with open('GPS.json', 'r') as g:
	# 获取到的数据为 [{},{}],处理为列表
	gps = json.load(g)

list_gps = []

for i in range(len(gps)):
	for value in gps[i].values():
		list_gps.append(value)

GPS = pd.DataFrame(list_gps, columns=['经纬度'])

# print(GPS)
# print(gps)

infoname = pd.read_csv('houseinfo.csv')
infoname = pd.DataFrame(infoname, columns=['name', 'place', 'price'])
# 将数据合并再写入csv文件
infos = pd.concat([infoname, GPS], axis=1)

# infos.to_csv('house.csv')

house = pd.read_csv('house.csv')
print(house)

if __name__ == '__main__':
	pass