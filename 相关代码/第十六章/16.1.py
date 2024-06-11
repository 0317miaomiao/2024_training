from pathlib import Path 
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('sitka_weather_07-2014.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines) 
header_row = next(reader)

# 提取并读取数据
waters = []
for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')
    water = int(row[5])
    highs.append(high)
    waters.append(water)

# 开始绘图
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, waters, color='red') 

# 设置绘图的格式
ax.set_title("Daily Water, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16) 

# 绘制倾斜的⽇期标签
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show() 
