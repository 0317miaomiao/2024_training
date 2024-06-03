# 定义文件名称
filename = 'learning_python.txt'

# 第一次打印时读取整个文件
with open(filename) as file_object:
    contents = file_object.read()
print("First read:")
print(contents)

# 第二次打印时先将所有行都存储在一个列表中，再遍历列表中的各行
print("\nSecond read:")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
