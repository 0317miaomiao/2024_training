import requests
import plotly.express as px

# 以C作为例子，其余的同理
url = "https://api.github.com/search/repositories?q=language:C+sort:stars+stars:>20000"
headers = {"Accept": "application/vnd.github.v3+json"} 
r = requests.get(url, headers=headers)

# 将响应转换为字典
response_dict = r.json()

# 研究仓库中的信息
repo_dicts = response_dict['items'] 
print(f"Repositories returned: {len(repo_dicts)}") 

# 研究第⼀个仓库
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}") 
for key in sorted(repo_dict.keys()): 
    print(key)

repo_names, stars, hover_texts = [], [], []
for repo_dict in repo_dicts: 
    repo_names.append(repo_dict['name']) 
    stars.append(repo_dict['stargazers_count'])
    
    # 创建悬停⽂本
    owner = repo_dict['owner']['login']
    description = repo_dict['description'] 
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 可视化
title = "Most-Starred Python Projects on GitHub" 
labels = {'x': 'Repository', 'y': 'Stars'} 
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels,hover_name=hover_texts) 
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
yaxis_title_font_size=20) 
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show() 
