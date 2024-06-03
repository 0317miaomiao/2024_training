class Restaurant:
    """一个描述餐厅的类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐厅属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """描述餐厅"""
        print(f"{self.restaurant_name} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        """显示一条消息，指出餐厅正在营业"""
        print(f"{self.restaurant_name} is open. Come on in!")

# 现在定义IceCreamStand类，它继承自Restaurant
class IceCreamStand(Restaurant):
    """描述冰激凌小店的类"""
    def __init__(self, name, cuisine_type='ice cream'):
        """初始化冰激凌小店属性"""
        super().__init__(name, cuisine_type)
        # 假设有一些默认的口味
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint']

    def show_flavors(self):
        """显示所有口味的冰激凌"""
        print(f"We have the following flavors available: {self.flavors}")

# 接下来创建IceCreamStand的实例
ice_cream_stand = IceCreamStand('The Sweet Cone')

# 调用describe_restaurant()和show_flavors()方法
ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()
