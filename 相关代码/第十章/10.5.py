name = ''
sum_name = ''

# 开始循环
while True:
    name = input("Please show me your name")
    if name == 'exit':
        break
    sum_name += f"{name} \n"

# 写入txt文件
path.write_text(sum_name)
