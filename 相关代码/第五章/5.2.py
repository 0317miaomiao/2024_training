# 检查两个字符串是否相等和不等
print("Is 'Python' == 'python'? I predict False.")
print('Python' == 'python')

print("\nIs 'Python' != 'JAVA'? I predict True.")
print('Python' != 'JAVA')

# 使用 lower() 方法的条件测试
print("\nIs 'Python'.lower() == 'python'? I predict True.")
print('Python'.lower() == 'python')

print("\nIs 'PYTHON'.lower() != 'python'? I predict False.")
print('PYTHON'.lower() != 'python')

# 涉及相等、不等、大于、小于、大于等于和小于等于的数值比较
number = 10
print("\nIs number == 10? I predict True.")
print(number == 10)

print("\nIs number != 10? I predict False.")
print(number != 10)

print("\nIs number > 5? I predict True.")
print(number > 5)

print("\nIs number < 5? I predict False.")
print(number < 5)

print("\nIs number >= 10? I predict True.")
print(number >= 10)

print("\nIs number <= 9? I predict False.")
print(number <= 9)

# 使用关键字 and 和 or 的条件测试
print("\nIs number > 5 and number < 15? I predict True.")
print(number > 5 and number < 15)

print("\nIs number < 5 or number > 15? I predict False.")
print(number < 5 or number > 15)

# 测试特定的值是否在列表中
colors = ['red', 'blue', 'green']
print("\nIs 'red' in colors? I predict True.")
print('red' in colors)

print("\nIs 'yellow' in colors? I predict False.")
print('yellow' in colors)

# 测试特定的值是否不在列表中
print("\nIs 'black' not in colors? I predict True.")
print('black' not in colors)

print("\nIs 'red' not in colors? I predict False.")
print('red' not in colors)
