import requests

def get_ip():
    # 定义获取 IP 地址的 API 的 URL
    API_URL = 'https://api.ipify.org'

    # 向 API 发送 GET 请求
    response = requests.get(API_URL)

    # 获取响应的文本，即 IP 地址
    ip_address = response.text

    # 打印 IP 地址
    print('当前的 IP 地址:', ip_address)

    # 以写入模式打开文件
    with open('ip.txt', 'w') as file:
        # 将 IP 地址写入文件
        file.write(ip_address)

if __name__ == "__main__":
    get_ip()
