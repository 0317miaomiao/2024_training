# 创建一个列表，其中包含前10个整数的立方
cubes = [number**3 for number in range(1, 11)]

# 使用一个for循环将这些立方数打印出来
for cube in cubes:
    print(cube)
