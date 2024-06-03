# 创建一个包含至少5个用户名的列表，其中一个用户名为 'admin'
usernames = ["admin", "Jaden", "Alice", "Bob", "Charlie"]

# 遍历用户名列表，向每个用户打印一条问候消息
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again")
