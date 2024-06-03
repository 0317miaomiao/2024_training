# 假定的favorite_languages字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 应该接受调查的人的名单
people_to_survey = ['jen', 'sarah', 'matt', 'daniela']

# 遍历名单
for person in people_to_survey:
    if person in favorite_languages.keys():
        print(f"Thank you, {person.title()}, for taking the survey.")
    else:
        print(f"{person.title()}, we invite you to take the favorite programming language survey.")
