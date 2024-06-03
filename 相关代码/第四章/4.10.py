# 创建一个包含1到20的奇数的列表
odd_numbers = list(range(1, 21, 2))

# 打印前三个元素
print("The first three items in the list are:")
print(odd_numbers[:3])

# 打印中间三个元素
middle_index = len(odd_numbers) // 2
print("Three items from the middle of the list are:")
print(odd_numbers[middle_index-1:middle_index+2])

# 打印最后三个元素
print("The last three items in the list are:")
print(odd_numbers[-3:])
