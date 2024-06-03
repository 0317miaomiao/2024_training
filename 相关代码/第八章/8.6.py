def city_country(city, country):
    # 返回城市和所属国家的格式化字符串
    return f"{city.title()}, {country.title()}"

# 使用三个城市-国家对调用这个函数，并打印返回的值
city_country_string1 = city_country('santiago', 'chile')
print(city_country_string1)

city_country_string2 = city_country('beijing', 'china')
print(city_country_string2)

city_country_string3 = city_country('paris', 'france')
print(city_country_string3)
