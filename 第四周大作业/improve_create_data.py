import os
import json
from sqlalchemy import create_engine, Column, Integer, String, LargeBinary, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declared_attr

# 配置数据库 URI
DATABASE_URI = 'mysql+mysqlconnector://root:hugo2468013579@localhost:3306/xiaomi_homework'

# 创建数据库引擎
engine = create_engine(DATABASE_URI, echo=False)
Base = declarative_base()

# 动态生成表结构
class Data(Base):
    __tablename__ = 'data_test'
    id = Column(Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def __table_args__(cls):
        return {'extend_existing': True}

    # 动态添加列
    @classmethod
    def add_columns(cls, column_names):
        for col_name in column_names:
            if col_name.endswith('_path'):
                setattr(cls, col_name, Column(String(255)))
                setattr(cls, col_name.replace('_path', '_content'), Column(LargeBinary))
            elif col_name.endswith('_timestamp') or col_name.endswith('_stamp'):
                setattr(cls, col_name, Column(String(20)))

# 读取 JSON 文件并提取键
with open('downloads/single-vehicle-side-example/data_info.json', 'r', encoding='utf-8') as f:
    data_list = json.load(f)
    if data_list:
        column_names = data_list[0].keys()

# 动态添加列
Data.add_columns(column_names)

# 创建数据表
Base.metadata.create_all(engine)

# 辅助函数来读取文件内容或大小
def get_file_content_or_size(file_path):
    full_path = os.path.join('downloads/single-vehicle-side-example', file_path)
    try:
        if os.path.exists(full_path):
            if full_path.endswith('.json') or full_path.endswith('.txt'):
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read().encode('utf-8')
            else:
                size = os.path.getsize(full_path)
                content = str(size).encode('utf-8')
        else:
            content = None
    except Exception as e:
        print(f"Error reading file {full_path}: {e}")
        content = None
    return content

# 创建会话（Session）
Session = sessionmaker(bind=engine)
session = Session()

# 插入数据
for data_dict in data_list:
    data_with_content = {}
    for key, value in data_dict.items():
        data_with_content[key] = value
        if key.endswith('_path'):
            # 加入可读文本的内容或者二进制文件大小
            content_key = key.replace('_path', '_content')
            data_with_content[content_key] = get_file_content_or_size(value)
    
    # 通过这种方式可以便捷的通过字典的方式整体插入内容
    new_data = Data(**data_with_content)
    session.add(new_data)

session.commit()
