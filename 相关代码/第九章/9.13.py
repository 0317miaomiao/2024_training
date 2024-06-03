import random

class Die:
    """表示一个骰子的类"""
    def __init__(self):
        """初始化骰子的属性"""
        self.sides = 6
        
    def roll_die(self):
        """返回一个位于1和骰子面数之间的随机数"""
        return random.randint(1, self.sides)

# 创建一个6面的骰子并掷10次
die_6 = Die()
print("10 rolls of a 6-sided die:")
for roll in range(10):
    print(die_6.roll_die(), end=' ')
print("\n")

# 创建一个10面的骰子并掷10次
Die.sides = 10
die_10 = Die()
print("10 rolls of a 10-sided die:")
for roll in range(10):
    print(die_10.roll_die(), end=' ')
print("\n")
