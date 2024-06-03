import json

def get_user_info():
    # 提示用户输入其信息
    username = input("What is your name? ")
    age = input("How old are you? ")
    favorite_color = input("What is your favorite color? ")
    return {
        'username': username,
        'age': age,
        'favorite_color': favorite_color,
    }

def save_user_info(user_info, filename='userinfo.json'):
    # 将用户信息存储到一个文件中
    with open(filename, 'w') as f:
        json.dump(user_info, f)

def load_user_info(filename='userinfo.json'):
    # 从文件中读取用户信息
    try:
        with open(filename) as f:
            user_info = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user_info
    
def remember_user():
    # 主程序流程
    user_info = get_user_info()
    save_user_info(user_info)
    loaded_user_info = load_user_info()
    if loaded_user_info:
        print(f"We remembered the following about you: {loaded_user_info}")

remember_user()
