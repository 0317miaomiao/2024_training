# 输入自己喜欢的数
number = input("write down the number that you like \t")

path = Path('numbers_like.json')
contents = json.dumps(number)
path.write_text(contents)

# 再从中读出这个名字
name = path.read_text()
use_name = json.loads(name)
print(use_name)
