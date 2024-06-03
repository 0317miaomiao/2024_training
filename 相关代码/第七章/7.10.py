# 创建一个空字典，用于存储调查结果
dream_vacation_spots = {}

poll_active = True

while poll_active:
    # 提问用户梦想的度假地
    name = input("\nWhat is your name? ")
    dream_spot = input("If you could visit one place in the world, where would you go? ")

    # 将答案存储在字典中
    dream_vacation_spots[name] = dream_spot

    # 询问是否还有其他人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'no':
        poll_active = False

# 调查结束，打印结果
print("\n--- Poll Results ---")
for name, dream_spot in dream_vacation_spots.items():
    print(f"{name.title()} would like to visit {dream_spot.title()}.")
