# 创建现存的用户名字
current_users = ["admin", "Jaden", "Alice", "Bob", "Charlie"]

# 创建新加入的用户名字
new_users = ["alice", "Eve", "charlie", "David", "Frank"]

# 创建 current_users 的副本，其中包含当前所有用户名的全小写版本
current_users_lower = [user.lower() for user in current_users]

# 遍历列表 new_users，检查其中的每个用户名是否已被使用
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"用户名 '{new_user}' 已被使用，请输入别的用户名。")
    else:
        print(f"用户名 '{new_user}' 未被使用，可以注册。")
