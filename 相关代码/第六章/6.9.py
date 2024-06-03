# 创建一个名为 favorite_places 的字典
favorite_places = {
    'Alice': ['Paris', 'New York', 'Tokyo'],
    'Bob': ['London', 'Berlin'],
    'Charlie': ['Sydney', 'San Francisco', 'Rome']
}

# 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来
for person, places in favorite_places.items():
    print(f"{person}喜欢的地方有:")
    for place in places:
        print(f"- {place}")
    print('\n')  
