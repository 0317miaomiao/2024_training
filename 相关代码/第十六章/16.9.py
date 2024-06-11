# 练习
path = Path('world_fires_7_day.csv')

# 读取数据，记为reader
lines = path.read_text().splitlines()
reader = csv.reader(lines)

# 提取其中的地点，时间，火灾亮度的数据，注意异常数据的处理
x_locations, y_locations, brightnesses = [], [], []
for row in reader:
    try:
        x_location = float(row[0])
        y_location = float(row[1])
        brightness = float(row[2])
    except ValueError:
        print("Some values are missed")
    else:
        x_locations.append(x_location)
        y_locations.append(y_location)
        brightnesses.append(brightness)

data = pd.DataFrame(data = zip(x_locations, y_locations, brightnesses), columns = ['x坐标','y坐标','亮度'])

# 开始绘图
# 因此图形的配置变成了
fig = px.scatter(data,
                 x = 'x坐标',
                 y = 'y坐标',
                 range_x=[-100,100],
                 range_y=[-100,100],
                 width=800,
                 height=800,
                 title = '火灾坐标图',
                size = '亮度',
                size_max=10,
                color = '亮度',
                )
fig.show()
