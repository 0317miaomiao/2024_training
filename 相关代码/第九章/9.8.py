# 创建priviliages 类
class Priviliages:
    
    def __init__(self, privileages):
        self.privileages = privileages
    
    # 构建问题2中的方法
    def show_priviliage(self):
        print(self.privileages)

# 继续使用问题3中构建好的类
class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        # 初始化继承的类
        super().__init__(first_name, last_name, age, email)
        
        # 添加一个priiviliages 的属性
        self.privileges = Priviliages(age)
    
user_1 = Admin('John', 'Doe', 28, 'johndoe@example.com')
user_1.privileges.show_priviliage()
