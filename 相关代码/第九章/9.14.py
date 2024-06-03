import random

# 创建一个包含10个数和5个字母的列表
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# 从列表中随机选择4个不同的数或字母
winning_elements = random.sample(elements, 4)

# 打印消息告知中奖的条件
print(f"如果彩票上是这4个数或字母{winning_elements}，你就中大奖了！")
