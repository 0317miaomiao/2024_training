your_pizzas = ["a", "b", "c"]
friend_pizzas = your_pizzas[:]

# 分别添加不同的pizza
your_pizzas.append("d")
friend_pizzas.append("e")

# 打印循环
for pizza in your_pizzas:
    print(f"My favorite pizzas are:{pizza}")

print("\n")

for pizza in friend_pizzas:
    print(f"My favorite pizzas are:{pizza}")
