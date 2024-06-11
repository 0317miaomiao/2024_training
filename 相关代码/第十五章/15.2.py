import matplotlib.pyplot as plt
import numpy as np

# 计算前5个正整数的立方值
x1 = list(range(1, 6))
y1 = [i**3 for i in x1]

# 计算前5000个正整数的立方值
x2 = list(range(1, 5001))
y2 = [i**3 for i in x2]

# 创建一个颜色映射
cmap = plt.get_cmap("viridis")

# 绘制前5个正整数的立方值，带颜色映射
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sc1 = plt.scatter(x1, y1, c=x1, cmap=cmap, edgecolor='k')
plt.colorbar(sc1, label='Value')
plt.title('Cubes of First 5 Positive Integers')
plt.xlabel('Number')
plt.ylabel('Cube Value')

# 绘制前5000个正整数的立方值，带颜色映射
plt.subplot(1, 2, 2)
sc2 = plt.scatter(x2, y2, c=x2, cmap=cmap, edgecolor='k', s=1)
plt.colorbar(sc2, label='Value')
plt.title('Cubes of First 5000 Positive Integers')
plt.xlabel('Number')
plt.ylabel('Cube Value')

# 显示图形
plt.show()
