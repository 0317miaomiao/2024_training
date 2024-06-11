from pathlib import Path 
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# 读取CSV文件并确定TMIN和TMAX列的索引
def read_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # 确定TMIN和TMAX列的索引
        tmin_index = header_row.index('Min TemperatureF')
        tmax_index = header_row.index('Max TemperatureF')

        # 读取数据
        tmin, tmax = [], []
        for row in reader:
            try: 
                min_temp = int(row[tmin_index])
                max_temp = int(row[tmax_index])
            except ValueError:
                print(f"Missing data for date_index")
            else:
                tmin.append(min_temp)
                tmax.append(max_temp)

    return tmin, tmax

# 绘制温度图
def plot_temperatures(tmin, tmax, station_name):
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    
    dates = list(range(len(tmax)))
    ax.plot(dates, tmax, c='red', alpha=0.5, label='TMAX')
    ax.plot(dates, tmin, c='blue', alpha=0.5, label='TMIN')
    plt.fill_between(dates, tmin, tmax, facecolor='blue', alpha=0.1)

    # 设置标题和标签
    plt.title(f"Daily high and low temperatures - {station_name}", fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.legend()

    plt.show()

# 主程序
file_path = 'death_valley_2014.csv'  
tmin, tmax = read_csv(file_path)
plot_temperatures(tmin, tmax, 'sitka')
