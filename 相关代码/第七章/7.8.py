# 创建一个包含各种三明治名字的列表
sandwich_orders = ['tuna sandwich', 'chicken sandwich', 'beef sandwich', 'vegetable sandwich']

# 创建一个空列表，用于存放已完成的三明治
finished_sandwiches = []

# 使用while遍历
while sandwich_orders != []:
    current_sand = sandwich_orders.pop()
    
    # 将值填入空列表中
    finished_sandwiches.append(current_sand)

print(finished_sandwiches)
