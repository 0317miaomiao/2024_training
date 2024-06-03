# 定义函数，其中country参数有一个默认值
def describe_city(city, country='China'):
    print(f"{city} is in {country}.")

# 调用函数
describe_city('Beijing')  # 使用默认国家
describe_city('Shanghai')  # 使用默认国家
describe_city('Reykjavik', 'Iceland')  # 指定国家，不使用默认值
