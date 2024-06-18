import requests
import zipfile

# 文件的实际下载URL
download_url = 'https://bj.bcebos.com/apollo-air/v2-2022-01-08/single-vehicle-side-example_16139952108871680.zip?authorization=bce-auth-v1%2F62ff93831d5840338d0fcc9585430b3a%2F2024-06-13T04%3A07%3A31Z%2F604800%2F%2Fd99cdee5b4618a8c1cf6e6f31ae7294dd0c4838d7a1e6f44bc07474066061e6d'

# 下载文件
response = requests.get(download_url, stream=True)
response.raise_for_status()  # 检查是否下载成功

# 保存下载的文件
with open('single-vehicle-side-example.zip', 'wb') as file:
    for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)

print('文件下载完成')


#定义保存的路径
save_path = './downloads'

# 
zip_file = 'single-vehicle-side-example.zip'

# 解压缩文件
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(save_path)
