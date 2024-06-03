# 创建一个名为 cities 的字典，将三个城市名用作键
cities = {
    'Paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'Paris is known as the "City of Light".'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '9.3 million',
        'fact': 'Tokyo is the largest metropolitan area in the world.'
    },
    'New York': {
        'country': 'USA',
        'population': '8.4 million',
        'fact': 'New York is known as "The Big Apple".'
    }
}

# 遍历字典，并将每座城市的名字以及相关信息打印出来
for city, info in cities.items():
    print(f"City: {city}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
