# 创建一个包含各种三明治名字的列表，并确保'pastrami'至少出现了三次
sandwich_orders = [
    'tuna sandwich', 'pastrami', 'chicken sandwich', 
    'beef sandwich', 'pastrami', 'vegetable sandwich', 'pastrami'
]

# 创建一个空列表，用于存放已完成的三明治
finished_sandwiches = []

# 打印消息，指出五香烟熏牛肉(pastrami)卖完了
print("Sorry, we're all out of pastrami today.")

# 使用while循环将列表sandwich_orders中的'pastrami'都删除
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# 遍历更新后的sandwich_orders列表
for sandwich in sandwich_orders:
    # 打印消息
    print(f"I made your {sandwich}.")
    # 将制作好的三明治移动到finished_sandwiches列表中
    finished_sandwiches.append(sandwich)

# 所有三明治都制作好后，打印消息
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
