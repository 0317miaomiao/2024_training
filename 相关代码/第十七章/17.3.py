import requests
import pytest

# 函数用于获取GitHub API的数据
def get_github_data():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    response = requests.get(url)
    return response

# 测试函数
def test_github_api_status_code():
    response = get_github_data()
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_github_api_total_repositories():
    response = get_github_data()
    response_dict = response.json()
    assert response_dict['total_count'] > 1000000, f"Expected total count > 1000000, but got {response_dict['total_count']}"


# 运行测试
if __name__ == "__main__":
    pytest.main()
