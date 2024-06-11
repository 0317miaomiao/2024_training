from pathlib import Path 
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.express as px
import pandas as pd

# 使用更多的数据
path = Path('eq_data_30_day_m1.geojson')
try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding='utf-8')

all_eq_data = json.loads(contents)

## 先转化为字典，再通过dunps以4格为缩进转化为json
## 这样子便于阅读
# 这里indent表示可以缩进多少
path = Path('readable_eq_data.geojson') 
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title'] 
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title) 
    lons.append(lon) 
    lats.append(lat)
print(mags[:10]) 
print(titles[:2]) 
print(lons[:5]) 
print(lats[:5])

data = pd.DataFrame((data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级'] )

# 因此图形的配置变成了
fig = px.scatter(data,
                 x = '经度',
                 y = '纬度',
                 range_x=[-200,200],
                 range_y=[-90,90],
                 width=800,
                 height=800,
                 title  = all_eq_data["metadata"]["title"]
                size = '震级',
                size_max=10,
                color = '震级',
                hover_name='位置')
fig.show()
           
