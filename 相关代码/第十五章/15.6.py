# 投掷两个骰子
# 创建两个D6 
die_1 = Die(8) 
die_2 = Die(8)

# 投掷多次
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
# 分析结果
frequencies = [] 
max_result = die_1.num_sides + die_2.num_sides

# 确定范围
poss_results = range(2, max_result+1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'} 
fig = px.bar(x=poss_results, y=frequencies, title=title, 
labels=labels) 

# 进⼀步定制图形
 
fig.update_layout(xaxis_dtick=1)

fig.show() 
