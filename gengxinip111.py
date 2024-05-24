import requests
import json

api_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJib3NzX2lkIjoiMTM0MjIzNjUxIiwiZGV2aWNlX3Rva2VuIjoiQTdMN212VjJFREgzOGtZbzl2dVdQdTJFIiwiZGV2aWNlX2lkIjoiTnpZMlpqY3hPVEl0WkdJMk5pMDBOVFkyTFRneVkyUXRNall3WkdGaE5tSm1NV1EzIiwiZGV2aWNlX3R5cGUiOiJ3ZWIiLCJkZXZpY2Vfb3MiOiJicm93c2VyIiwiZHJtX2lkIjoiTnpZMlpqY3hPVEl0WkdJMk5pMDBOVFkyTFRneVkyUXRNall3WkdGaE5tSm1NV1EzIiwiZXh0cmEiOnsicHJvZmlsZV9pZCI6MX0sImlhdCI6MTcxNjQ2MzQ5NCwiZXhwIjoxNzE2NDY3MDk0fQ.EiwCYPH3a6tRpHkO2cOe4bwd4jPVkWmbyjNqSLU5P3FY7YzWhunag8TQYGfwlx8VjVqYkZf8fXK3sqw3AVwzybPWPT13svVgVj7g5QF48TArIIymgC_sgaoYOMv4VAErHYBTQHdRIwPqB82jbqpMH333gwREeiiqmqa6RAhWtLzuFqZsXXXbfNtOL7kXp7M-HWQTCsZRI52DJNVfH-SW4F5j83FzF8CEEgL15a1C7Tk-ute0iBjueay72v67xWlbN8ltRICZdOvWMwapoAY8v1hAn202muuWM_xNmeJN9zT3qWjFA6nGS6gSZNFVTenL_35hBz1O9QRLD9PnRZCxJJ6ypUp4Ts1Oi_36PGYd6WDYYhWEqYsDapDILt0iRMLJpXHg1M-VGzX4z1RRqhSt5fwLvY1Gizjb0y6i9ojtmgbSb5xsfOe6kPh9ipazmnOUQ9ENh98iNPRoQszBHT1D6ZQ6qKKiCx_o99rpWTdJfFXzZsmdWgopcxnPI6U6d9MxcbcOx5tRDTQXyUqtnsNxKk1sedgWTN1yR26-HsPVsMYJ4Bl5q74A8bh-6S2M6-b0vrQ-UiEMHhumZTRGCwxXS-dFJGocFeOpjSRuLed286CLUuMigoIhr9dWoP8tID4PIrRGWwU7a-C0ea_SO_9KXhXeZlny1S0pylegdo8uuuo'

def get_mytvsuper(channel):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Host': 'user-api.mytvsuper.com',
        'Origin': 'https://www.mytvsuper.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.15',
        'Referer': 'https://www.mytvsuper.com/',
        'X-Forwarded-For': '210.6.4.148', 
    }

    params = {
        'platform': 'android_tv',
        'network_code': channel
    }

    response = requests.get('https://user-api.mytvsuper.com/v1/channel/checkout', headers=headers, params=params)
    if response.status_code != 200:
        return None

    json_data = response.json()
    profiles = json_data.get('profiles', [])
    play_url = ''
    for i in profiles:
        if i.get('quality') == 'high':
            play_url = i.get('streaming_path')
            break

    if not play_url:
        return None
    return play_url.split('&p=')[0]

def handle_request(id):
    redirect_url = get_mytvsuper(id) or 'https://nolive.livednow.com/nolive.m3u8'
    return redirect_url

print(handle_request('your_id_here'))  # replace 'your_id_here' with the actual id
