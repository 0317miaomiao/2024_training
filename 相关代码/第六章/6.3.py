# 创建一个词汇表字典，包含编程术语及其含义
vocabulary = {
    "variable": "A storage location in programming that holds a value.",
    "function": "A block of code that performs a specific task and can be called when needed.",
    "loop": "A sequence of instructions that is continually repeated until a certain condition is reached.",
    "list": "A collection of items in a particular order.",
    "dictionary": "A collection of key-value pairs, where each key is associated with a value."
}

# 以整洁的方式打印每个术语及其含义，用items可以来两个一次遍历
for term, definition in vocabulary.items():
    print(f"{term}:\n\t{definition}\n")
