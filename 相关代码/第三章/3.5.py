# 确定哪位嘉宾无法赴约
unable_to_attend = "Albert"
print(f"{unable_to_attend} can not attend dinner")

# 确定新嘉宾的名单
new_attend = "David"

# 修改嘉宾名单，替换无法赴约的嘉宾
guest_list[guest_list.index(unable_to_attend)] = new_attend

# 再次打印邀请消息
for guest in guest_list:
    message = f"Dear {guest}, I would be honored to have you join me for dinner."
    print(message)
