def print_pet_names(filename):
    """尝试读取并打印文件中宠物的名字"""
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"抱歉，找不到文件 {filename}。")
    else:
        print(f"{filename} 中的宠物名字有：")
        print(contents)

# 尝试读取并打印文件内容
print_pet_names('cats.txt')
print_pet_names('dogs.txt')
