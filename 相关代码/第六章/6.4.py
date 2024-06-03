# 初始化词汇表字典，包含一些Python术语及其解释
glossary = {
    'list': 'A collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'The action of doing something over and over again.',
    'variable': 'A label for a value.',
    'string': 'A series of characters.'
}

# 添加5个新的Python术语
glossary['function'] = 'A named set of instructions that defines a set of actions in Python.'
glossary['tuple'] = 'An immutable list of values.'
glossary['boolean'] = 'A data type that can hold one of two values: True or False.'
glossary['slice'] = 'A specific part or segment of a list or string.'
glossary['argument'] = 'A value that is passed to a function when calling it.'

# 遍历词汇表的键和值，打印出术语及其解释
for term, definition in glossary.items():
    print(f"{term.title()}: {definition}")
