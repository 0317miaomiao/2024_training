# 定义一个可接受任意数量食材的函数
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    print("Your sandwich is ready!\n")

# 第一次调用函数，提供三种食材
make_sandwich('ham', 'cheese', 'tomato')

# 第二次调用函数，提供两种食材
make_sandwich('turkey', 'avocado')

# 第三次调用函数，提供四种食材
make_sandwich('chicken', 'lettuce', 'mayo', 'mustard')
