# 定义变量来表示一个人的名字，并在其开头和末尾包含一些空白字符
name = "\t Eric \n"

# 使用lstrip()函数删除开头的空白字符
name_lstrip = name.lstrip()
print(f"使用lstrip()处理后：'{name_lstrip}'")

# 使用rstrip()函数删除末尾的空白字符
name_rstrip = name.rstrip()
print(f"使用rstrip()处理后：'{name_rstrip}'")

# 使用strip()函数删除开头和末尾的空白字符
name_strip = name.strip()
print(f"使用strip()处理后：'{name_strip}'")
