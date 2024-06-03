class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    # 构建两个相关的函数
    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")
    
    def open_restaurant(self):
        print("Normal")
print(restaurant = Restaurant("Miqilin", "Normal"))
print(restaurant.restaurant_name)
