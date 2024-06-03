filename = 'learning_python.txt'

print("\nModified lines:")
# 读取learning_python.txt中的每一行
with open(filename) as file_object:
    lines = file_object.readlines()

# 遍历每一行，替换'Python'为'C'并打印到屏幕上
for line in lines:
    modified_line = line.replace('Python', 'C')
    print(modified_line.rstrip())
