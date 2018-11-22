import json

import requests
import pandas as pd
# 申请的key(判定服务为web服务)
ak = '36957fce2131c9571666ad2bed290d56'


# 传入地址，返回对应地址的经纬度信息
def address_gps(address):
	url = "http://restapi.amap.com/v3/geocode/geo?key=%s&address=%s" % (ak, address)
	data = requests.get(url)
	contest = data.json()
	try:
		# 传入的地址可能获取不到经纬度
		contest = contest['geocodes'][0]['location']
		return contest
	except:
		return None


infoname = pd.read_csv('houseinfo.csv')
names = infoname['name'].to_dict()
GPS = []

# 循环遍历csv文件的地址
for i in names.keys():
	name = names[i]
	# 将获取到的经纬度转化为浮点型
	GPS.append(address_gps(name))

with open('GPS.json', 'w') as g:
	json.dump(GPS, g)

if __name__ == '__main__':
	pass