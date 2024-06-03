# 创建一个包含数字1到1,000,000的列表
numbers = list(range(1, 1000001))

# 使用min()和max()核实列表确实是从1开始到1,000,000结束的
print("最小值：", min(numbers))
print("最大值：", max(numbers))

# 对这个列表调用sum()，计算1到1,000,000的总和
print("总和：", sum(numbers))
