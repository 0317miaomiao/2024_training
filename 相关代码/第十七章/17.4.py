import requests
import plotly.express as px

# GitHub API URL
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# 发送请求并获取响应
response = requests.get(url)
response_dict = response.json()

# 提取仓库信息
repo_dicts = response_dict['items']
repo_names = [repo['name'] for repo in repo_dicts]
stars = [repo['stargazers_count'] for repo in repo_dicts]
descriptions = [repo['description'] for repo in repo_dicts]
repo_links = [repo['html_url'] for repo in repo_dicts]


# 创建条形图
fig = px.bar(
    x=repo_names,
    y=stars,
    title='Most Popular Python Projects on GitHub',
    labels={'x': 'Repository', 'y': 'Stars'},
    hover_name=descriptions
)

# 定制图形样式
fig.update_layout(
    title_font_size=24,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
    xaxis_tickangle=-45,
    template='plotly_dark'
)

# 为每个条形添加链接
for i, link in enumerate(repo_links):
    fig.data[0].text[i] = f'<a href="{link}">{repo_names[i]}</a>'

fig.show()
