# 使用字典来存储一些人喜欢的数
favorite_numbers = {
    'Alice': 12,
    'Bob': 8,
    'Charlie': 3,
    'Diana': 7,
    'Evan': 42,
}

# 打印每个人的名字和喜欢的数
for name, number in favorite_numbers.items():
    print(f"{name} likes the number {number}.")
