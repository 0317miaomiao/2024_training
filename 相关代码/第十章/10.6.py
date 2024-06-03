print("请输入两个数，我将计算它们的和。")
print("输入'q'退出。")

while True:
    first_number = input("\n第一个数：")
    if first_number == 'q':
        break
    second_number = input("第二个数：")
    if second_number == 'q':
        break
        
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("错误：请输入数值。")
    else:
        print(f"{first_number} + {second_number} = {answer}")
