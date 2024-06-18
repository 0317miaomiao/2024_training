import json
import os
from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建数据库连接
DATABASE_URI = 'mysql+mysqlconnector://root:hugo2468013579@localhost:3306/xiaomi_homework'
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()

# 定义数据模型类
class Data(Base):
    __tablename__ = 'data_test'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_path = Column(String(255))
    image_timestamp = Column(String(20))
    pointcloud_path = Column(String(255))
    point_cloud_stamp = Column(String(20))
    calib_camera_intrinsic_path = Column(String(255))
    calib_lidar_to_camera_path = Column(String(255))
    label_camera_std_path = Column(String(255))
    label_lidar_std_path = Column(String(255))
    image_content = Column(LargeBinary)
    pointcloud_content = Column(LargeBinary)
    calib_camera_intrinsic_content = Column(LargeBinary)
    calib_lidar_to_camera_content = Column(LargeBinary)
    label_camera_std_content = Column(LargeBinary)
    label_lidar_std_content = Column(LargeBinary)

# 创建数据表
Base.metadata.create_all(engine)

# 读取 JSON 文件并插入数据
with open('downloads/single-vehicle-side-example/data_info.json', 'r', encoding='utf-8') as f:
    data_list = json.load(f)

# 创建会话（Session）
Session = sessionmaker(bind=engine)
session = Session()

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

# 插入数据
for index, data_dict in enumerate(data_list):
    data_with_content = {}
    # 首先判断是否有缺失的列
    # 第一组的值是检查过没有问题的
    if len(data_dict) == len(data_list[0]):
        for key, value in data_dict.items():
            data_with_content[key] = value
            if key.endswith('_path'):
                # 加入可读文本的内容或者二进制文件大小
                content_key = key.replace('_path', '_content')
                data_with_content[content_key] = get_file_content_or_size(value)
        
        # 判断字典中是否有空值
        none_values = {k: v for k, v in data_with_content.items() if v is None}
        if none_values:
            print(f"第{index+1}组存在空值")
            for key, value in none_values.items():
                print(f"空值的列为{key}")
        else:
            # 通过这种方式可以便捷的通过字典的方式整体插入内容
            new_data = Data(**data_with_content)
            session.add(new_data)
    else:
        print(f"第{index+1}组存在缺失列")

session.commit()


# 查询所有数据
query = session.query(Data).all()

# 打印结果
for data in query:
    print(f"ID: {data.id}")
    print(f"Image Path: {data.image_path}")
    print(f"Image Timestamp: {data.image_timestamp}")
    print(f"Pointcloud Path: {data.pointcloud_path}")
    print(f"Point Cloud Stamp: {data.point_cloud_stamp}")
    print(f"Calib Camera Intrinsic Path: {data.calib_camera_intrinsic_path}")
    print(f"Calib Lidar to Camera Path: {data.calib_lidar_to_camera_path}")
    print(f"Label Camera Std Path: {data.label_camera_std_path}")
    print(f"Label Lidar Std Path: {data.label_lidar_std_path}")
    print(f"{data.image_content.decode('utf-8')}")
    print(f"{data.calib_camera_intrinsic_content.decode('utf-8')}")
    
    print("----------------------")
