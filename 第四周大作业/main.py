from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, LargeBinary
import os
from fastapi.responses import JSONResponse, FileResponse

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

# 创建会话（Session）
Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()

@app.get("/data/image/{image_path:path}")
async def get_data_by_image_path(image_path: str):
    print(f"Received request for image path: {image_path}")
    data = session.query(Data).filter(Data.image_path == image_path).first()
    if data:
        print(f"Found data for image path: {data.image_path}")
        return {
            "image_path": data.image_path,
            "image_timestamp": data.image_timestamp,
            "pointcloud_path": data.pointcloud_path,
            "point_cloud_stamp": data.point_cloud_stamp,
            "calib_camera_intrinsic_path": data.calib_camera_intrinsic_path,
            "calib_lidar_to_camera_path": data.calib_lidar_to_camera_path,
            "label_camera_std_path": data.label_camera_std_path,
            "label_lidar_std_path": data.label_lidar_std_path,
            "calib_camera_intrinsic_content": data.calib_camera_intrinsic_content.decode('utf-8') if data.calib_camera_intrinsic_content else None,
            "calib_lidar_to_camera_content": data.calib_lidar_to_camera_content.decode('utf-8') if data.calib_lidar_to_camera_content else None,
            "label_lidar_std_content": data.label_lidar_std_content.decode('utf-8') if data.label_lidar_std_content else None
        }
    else:
        print("Data not found")
        raise HTTPException(status_code=404, detail="Data not found")

# 设置图片目录
IMAGE_DIR = 'downloads/single-vehicle-side-example/image'

# 检查图片文件是否存在
def check_image_file(filename):
    return os.path.isfile(os.path.join(IMAGE_DIR, filename))

# 查询接口：返回图片文件的下载地址和参数
@app.get('/query_image/{image_name}', response_class=JSONResponse)
async def query_image(image_name: str):
    if check_image_file(image_name):
        download_url = f'download_image/{image_name}'
        return {"message": "Image available", "download_url": f"http://localhost:8000/{download_url}"}
    else:
        raise HTTPException(status_code=404, detail="Image not found")

# 图片查看和下载接口：提供图片文件
@app.get('/download_image/{image_name}', response_class=FileResponse)
async def download_image(image_name: str):
    file_path = os.path.join(IMAGE_DIR, image_name)
    if check_image_file(image_name):
        return FileResponse(file_path, filename=image_name)
    else:
        raise HTTPException(status_code=404, detail="Image not found")
        

# 启动 FastAPI 服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
