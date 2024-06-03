# 询问用户有多少人用餐
number_of_guests = input("您有多少人用餐？ ")

# 将输入转换为整数
number_of_guests = int(number_of_guests)

# 判断是否有空桌
if number_of_guests > 8:
    print("对不起，目前没有空桌。")
else:
    print("有空桌，请跟我来。")
