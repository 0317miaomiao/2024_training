import random

# 创建一个包含10个数和5个字母的列表
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# 定义你的彩票
my_ticket = [2, 6, 'b', 'e']

# 用于记录尝试次数的变量
tries = 0

# 循环，直到选出的组合与你的彩票完全匹配
while True:
    tries += 1
    winning_elements = random.sample(elements, 4)
    if sorted(winning_elements) == sorted(my_ticket):
        break

# 打印报告
print(f"中大奖需要尝试了{tries}次。")
