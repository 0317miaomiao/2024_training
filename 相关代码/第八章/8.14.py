# 定义函数，可以储存任意变量的实参
def make_car(maker, type_car, **car_info):
    car_info['car_maker'] = maker
    car_info['typecar'] = type_car
    return car_info

# 打印相关值
make_car('subaru', 'outback', color='blue', tow_package=True)
