from random import randint
import plotly.express as px 

class Die:
    """构建一个骰子类"""
    
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides
    
    def roll(self):
        """返回一个1到6之间的随机值"""
        return randint(1, self.num_sides)

# 投掷两个骰子
# 创建两个D6 
die_1 = Die() 
die_2 = Die()

# 投掷多次
results = [die_1.roll() + die_2.roll() for _ in range(1000)]
    
# 分析结果

max_result = die_1.num_sides + die_2.num_sides

# 确定范围
poss_results = range(2, max_result+1)

frequencies = [results.count(value) for value in poss_results]

# 可视化
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'} 
fig = px.bar(x=poss_results, y=frequencies, title=title, 
labels=labels) 

# 进⼀步定制图形
 
fig.update_layout(xaxis_dtick=1)

fig.show() 
