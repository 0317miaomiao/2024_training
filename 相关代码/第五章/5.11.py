# 在一个列表中存储数字 1-9
numbers = list(range(1, 10))

# 遍历这个列表
for number in numbers:
    # 使用 if-elif-else 结构，打印每个数字对应的序数
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
