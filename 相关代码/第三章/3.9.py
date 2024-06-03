# 指出你只能邀请两位嘉宾共进晚餐
print("Unfortunately, the new dining table won't arrive in time, so I can only invite two guests.\n")

# 不断地删除名单中的嘉宾，直到只有两位嘉宾为止
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Dear {removed_guest}, I am very sorry, but I can no longer invite you to dinner.")

# 对于余下两位嘉宾，打印消息指出他们依然在受邀之列
for guest in guest_list:
    print(f"Dear {guest}, you are still invited to dinner.")

# 使用 del 将最后两位嘉宾从名单中删除，让名单变成空的
del guest_list[0]
del guest_list[0]

# 打印该名单，核实名单在程序结束时确实是空的
print(f"\nFinal guest list: {guest_list}")

# 打印有多少嘉宾
print(len(guest_list))
