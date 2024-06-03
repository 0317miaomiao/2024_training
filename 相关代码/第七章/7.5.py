# 循环询问用户的年龄并指出票价
print("请输入您的年龄来确定电影票价：")
print("（输入 'quit' 结束）")

while True:
    age_input = input("您的年龄：")
    if age_input.lower() == 'quit':
        break

    age = int(age_input)
    
    if age < 3:
        print("您的电影票免费。")
    elif age <= 12:
        print("您的电影票价格是10美元。")
    else:
        print("您的电影票价格是15美元。")
