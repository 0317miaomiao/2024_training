# 循环提示用户输入比萨配料
print("请输入您希望添加到比萨中的配料：")
print("（输入 'quit' 结束）")

while True:
    ingredient = input("> ")
    if ingredient == 'quit':
        break
    else:
        print(f"我们会在比萨中添加{ingredient}。")
