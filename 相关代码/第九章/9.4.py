class Restaurant:
    """描述餐馆的类"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆的名称、菜系以及就餐人数"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # 添加的就餐人数属性，默认值为0
        
    def describe_restaurant(self):
        """显示餐馆信息的方法"""
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        """显示餐馆正在营业的消息"""
        print(f"{self.restaurant_name} is now open for business!")
        
    def set_number_served(self, number):
        """设置就餐人数的方法"""
        self.number_served = number
        
    def increment_number_served(self, additional_served):
        """让就餐人数递增的方法"""
        self.number_served += additional_served

# 创建Restaurant类的实例
restaurant = Restaurant('The Great Wall', 'Chinese')

# 初始就餐人数
print(f"Number served: {restaurant.number_served}")

# 修改就餐人数
restaurant.number_served = 10
print(f"Number served after modification: {restaurant.number_served}")

# 使用set_number_served()方法设置新的就餐人数
restaurant.set_number_served(20)
print(f"Number served after calling set_number_served(): {restaurant.number_served}")

# 使用increment_number_served()方法递增就餐人数
restaurant.increment_number_served(15)
print(f"Number served after calling increment_number_served(): {restaurant.number_served}")
