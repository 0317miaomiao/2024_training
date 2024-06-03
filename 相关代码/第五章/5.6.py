# 设置年龄变量
age = 25

# 使用 if-elif-else 结构根据年龄判断人生阶段
if age < 2:
    print("这个人是婴儿。")
elif age >= 2 and age < 4:
    print("这个人是幼儿。")
elif age >= 4 and age < 13:
    print("这个人是儿童。")
elif age >= 13 and age < 18:
    print("这个人是少年。")
elif age >= 18 and age < 65:
    print("这个人是中青年人。")
else:  # age >= 65
    print("这个人是老年人。")
