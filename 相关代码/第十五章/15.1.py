import matplotlib.pyplot as plt

# 计算前5个正整数的立方值
x1 = list(range(1, 6))
y1 = [i**3 for i in x1]

# 计算前5000个正整数的立方值
x2 = list(range(1, 5001))
y2 = [i**3 for i in x2]

# 绘制前5个正整数的立方值
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x1, y1, marker='o', linestyle='-', color='b')
plt.title('Cubes of First 5 Positive Integers')
plt.xlabel('Number')
plt.ylabel('Cube Value')

# 绘制前5000个正整数的立方值
plt.subplot(1, 2, 2)
plt.plot(x2, y2, linestyle='-', color='r')
plt.title('Cubes of First 5000 Positive Integers')
plt.xlabel('Number')
plt.ylabel('Cube Value')

# 显示图形
plt.tight_layout()
plt.show()
