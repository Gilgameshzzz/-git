import random
import pandas as pd

gps = pd.read_csv('gps.csv')

gps = gps['经纬度'].tolist()

for i in range(len(gps)):
    j = random.randint(100, 15000)
    gps[i] =  str(j) + '$' + gps[i]

with open('new_gps.js', 'w') as g:
    g.write(str(gps))
    print('ok')