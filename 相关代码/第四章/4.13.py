# 存储5种简单的食品在一个元组中
menu_items = ('pizza', 'salad', 'soup', 'sandwich', 'pasta')

# 使用一个for循环将餐馆提供的5种食品都打印出来
print("Original menu:")
for item in menu_items:
    print(item)
    
# 尝试修改其中一个元素
# menu_items[0] = 'sushi'  # 这行代码如果取消注释将会导致错误

# 餐馆调整菜单，替换了两种食品
menu_items = ('sushi', 'salad', 'soup', 'steak', 'ice cream')

# 使用一个for循环将新元组的每个元素都打印出来
print("\nUpdated menu:")
for item in menu_items:
    print(item)
