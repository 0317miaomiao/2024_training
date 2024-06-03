path = Path('guest_book.json')
user_info_temp = ''

while True:
    name = input("Please enter your name (enter 'q' to quit): ")
    if name == 'q':
        break
    email = input("Please enter your email: ")
    age = input("Please enter your age: ")
    
    # 将用户信息存储到字典中
    user_info = {
        'name': name,
        'email': email,
        'age': age,
    }
    user_info_temp += f"{user_info} \n"
    
contents = json.dumps(user_info_temp)
# 写入内容
path.write_text(contents)

# 读取文件内容，并解析JSON数据
try:
    name = path.read_text()
    use_name = json.loads(name)
    for line in use_name:
        print(line)
except FileNotFoundError:
    print(f"The file does not exist.")
