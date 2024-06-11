import matplotlib.pyplot as plt
import random

# 定义Die类
class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)

# 投掷两个骰子
# 创建两个D6 
die_1 = Die() 
die_2 = Die()

# 投掷多次
results = [die_1.roll() + die_2.roll() for _ in range(1000)]

# 分析结果
max_result = die_1.num_sides + die_2.num_sides

# 确定范围
poss_results = range(2, max_result + 1)

# 使用列表推导式计算频率
frequencies = [results.count(value) for value in poss_results]

# 可视化
plt.style.use('classic')
fig, ax = plt.subplots()

ax.bar(poss_results, frequencies, color='blue')

# 设置标题和标签
ax.set_title("Results of Rolling Two D6 Dice 1,000 Times", fontsize=14)
ax.set_xlabel("Result", fontsize=12)
ax.set_ylabel("Frequency of Result", fontsize=12)

# 设置x轴的刻度
ax.set_xticks(poss_results)

# 显示图形
plt.show()
