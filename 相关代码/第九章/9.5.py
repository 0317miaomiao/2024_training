class User:
    def __init__(self, first_name, last_name, age, email):
        """初始化用户"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """打印用户信息摘要"""
        print(f"User Profile:")
        print(f"- First name: {self.first_name}")
        print(f"- Last name: {self.last_name}")
        print(f"- Age: {self.age}")
        print(f"- Email: {self.email}")

    def greet_user(self):
        """向用户发出个性化问候"""
        print(f"Hello {self.first_name} {self.last_name}, welcome back!")
    
    # 让login_attempt +1
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    # 归0
    def reset_login_attempts() :
        self.login_attempts = 0

# 使用User类创建一个实例
user_1 = User('John', 'Doe', 28, 'johndoe@example.com')

# 调用方法describe_user()和greet_user()
print(user_1.describe_user())
print(user_1.greet_user())
print(user_1.increment_login_attempts())
print(user_1.increment_login_attempts())
print(user_1.login_attempts)
