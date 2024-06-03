# 在while循环中使用条件测试来结束循环
age_input = ""
while age_input.lower() != 'quit':
    age_input = input("请输入您的年龄（输入 'quit' 结束）：")
    
    if age_input.lower() == 'quit':
        continue
        
    age = int(age_input)
    if age < 3:
        print("您的电影票免费。")
    elif age <= 12:
        print("您的电影票价格是10美元。")
    else:
        print("您的电影票价格是15美元。")


#####################################################

# 使用变量active来控制循环结束的时机
active = True
while active:
    age_input = input("请输入您的年龄（输入 'quit' 结束）：")
    if age_input.lower() == 'quit':
        active = False
    else:
        age = int(age_input)
        if age < 3:
            print("您的电影票免费。")
        elif age <= 12:
            print("您的电影票价格是10美元。")
        else:
            print("您的电影票价格是15美元。")


#####################################################

# 使用break语句在用户输入'quit'时退出循环
while True:
    age_input = input("请输入您的年龄（输入 'quit' 结束）：")
    if age_input.lower() == 'quit':
        break

    age = int(age_input)
    if age < 3:
        print("您的电影票免费。")
    elif age <= 12:
        print("您的电影票价格是10美元。")
    else:
        print("您的电影票价格是15美元。")
