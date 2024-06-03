# 原有的字典，存储第一个人的信息
person_info_1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York',
}

# 创建两个新的字典，分别代表其他两个人的信息
person_info_2 = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 25,
    'city': 'Los Angeles',
}

person_info_3 = {
    'first_name': 'Jim',
    'last_name': 'Bean',
    'age': 32,
    'city': 'Chicago',
}

# 将这三个字典都存储在一个名为people的列表中
people = [person_info_1, person_info_2, person_info_3]

# 遍历people列表，将其中每个人的所有信息都打印出来
for person_info in people:
    print(f"\nFirst name: {person_info['first_name']}")
    print(f"Last name: {person_info['last_name']}")
    print(f"Age: {person_info['age']}")
    print(f"City: {person_info['city']}")
