import requests
import plotly.express as px
from operator import itemgetter
import json

url = "https://hacker-news.firebaseio.com/v0/topstories.json" 
r = requests.get(url) 
print(f"Status code: {r.status_code}") 

#处理有关每篇⽂章的信息
submission_ids = r.json() 
submission_dicts = []
for submission_id in submission_ids[:30]: 
    # 对于每篇⽂章，都执⾏⼀个API 调⽤
    url = f"https://hackernews.firebaseio.com/v0/item/{submission_id}.json" 
    r = requests.get(url) 
    response_dict = r.json() 
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        # 忽略没有评论数的文章（如招聘帖）
        continue
        
# 按照评论进行排序
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# 提取数据
titles = [submission['title'] for submission in submission_dicts]
comments = [submission['comments'] for submission in submission_dicts]
links = [submission['hn_link'] for submission in submission_dicts]

# 创建条形图
fig = px.bar(
    x=titles,
    y=comments,
    title='Most Active Discussions on Hacker News',
    labels={'x': 'Article Title', 'y': 'Number of Comments'},
    hover_name=links
)

# 定制图形样式
fig.update_layout(
    title_font_size=24,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
    xaxis_tickangle=-45,
    template='plotly_white'
)

# 为每个条形添加链接
fig.update_traces(text=[f'<a href="{link}">{title}</a>' for title, link in zip(titles, links)], textposition='outside')

fig.show()
