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
        print("错误：请输入数值，文本无法进行加法运算。请尝试再次输入数字。")
    else:
        print(f"{first_number} + {second_number} = {answer}")
        # 如果成功，跳出循环，或者稍作修改可以询问用户是否继续
        break  # 可以删除这一行，如果你想让用户继续输入新的数值
        
        
