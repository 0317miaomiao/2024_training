import json

def get_stored_username(filename='userinfo.json'):
    # 如果存储了用户名，就获取它
    try:
        with open(filename) as f:
            userinfo = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return userinfo

def get_new_username(filename='userinfo.json'):
    # 提示用户输入新的用户名
    username = input("What is your name? ")
    userinfo = {'username': username}
    with open(filename, 'w') as f:
        json.dump(userinfo, f)
    return userinfo

def greet_user(filename='userinfo.json'):
    # 问候用户，并指出其姓名
    userinfo = get_stored_username(filename)
    if userinfo:
        correct = input(f"Are you {userinfo['username']}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {userinfo['username']}!")
        else:
            userinfo = get_new_username(filename)
            print(f"We'll remember you when you come back, {userinfo['username']}!")
    else:
        userinfo = get_new_username(filename)
        print(f"We'll remember you when you come back, {userinfo['username']}!")

greet_user()
