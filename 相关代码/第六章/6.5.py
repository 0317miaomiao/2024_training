# 创建一个字典，存储三条河流及其流经的国家
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# 使用循环为每条河流打印一条消息
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# 使用循环将该字典中每条河流的名字打印出来
print("Rivers:")
for river in rivers.keys():
    print(river.title())

# 使用循环将该字典包含的每个国家的名字打印出来
print("Countries:")
for country in rivers.values():
    print(country.title())
