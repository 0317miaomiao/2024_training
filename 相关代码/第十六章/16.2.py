from pathlib import Path 
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# 生成雨林的相关数据
path = Path('sitka_weather_2014.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines) 
header_row = next(reader)

highs = []
dates= []
for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')
    high = int(row[4])
    highs.append(high)
    dates.append(current_date)

# 开始绘图
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red') 

# 设置绘图的格式
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16) 

# 绘制倾斜的⽇期标签
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

# 改变y轴坐标，对于死亡谷的数据同理
plt.ylim(50,150)

plt.show() 
    
