# 创建多个表示宠物的字典，每个字典都包含宠物的类型及其主人的名字
pet1 = {'type': 'dog', 'owner': 'Alice'}
pet2 = {'type': 'cat', 'owner': 'Bob'}
pet3 = {'type': 'rabbit', 'owner': 'Charlie'}

# 将这些字典存储在一个名为 pets 的列表中
pets = [pet1, pet2, pet3]

# 遍历该列表，并将有关每个宠物的所有信息打印出来
for pet in pets:
    print(f"Pet Type: {pet['type'].title()}, Owner: {pet['owner'].title()}")
