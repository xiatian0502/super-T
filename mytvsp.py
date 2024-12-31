import requests
import json

CHANNEL_LIST = {
    'J': {
        'name': '翡翠台',
        'license': '0958b9c657622c465a6205eb2252b8ed:2d2fd7b1661b1e28de38268872b48480',
        'logo': 'https://github.com/wanglindl/TVlogo/blob/main/img/TVB1.png?raw=true',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=0958b9c657622c465a6205eb2252b8ed&key=2d2fd7b1661b1e28de38268872b48480'
    },
    'JUHD': {
        'name': '翡翠台 4K',
        'license': '2c045f5adb26d391cc41cd01f00416fa:fc146771a9b096fc4cb57ffe769861be',
        'logo': 'https://github.com/wanglindl/TVlogo/blob/main/img/TVB1.png?raw=true',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=2c045f5adb26d391cc41cd01f00416fa&key=fc146771a9b096fc4cb57ffe769861be'
    },
    'B': {
        'name': 'TVBplus',
        'license': '56603b65fa1d7383b6ef0e73b9ae69fa:5d9d8e957d2e45d8189a56fe8665aaaa',
        'logo': 'https://raw.githubusercontent.com/wanglindl/TVlogo/main/img/TVB3.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=56603b65fa1d7383b6ef0e73b9ae69fa&key=5d9d8e957d2e45d8189a56fe8665aaaa'
    },
    'P': {
        'name': '明珠台',
        'license': 'e04facdd91354deee318c674993b74c1:8f97a629de680af93a652c3102b65898',
        'logo': 'https://github.com/wanglindl/TVlogo/blob/main/img/TVB1.png?raw=true',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=e04facdd91354deee318c674993b74c1&key=8f97a629de680af93a652c3102b65898'
    },
    'CWIN': {
        'name': 'Super Free',
        'license': '0737b75ee8906c00bb7bb8f666da72a0:15f515458cdb5107452f943a111cbe89',
        'logo': 'https://raw.githubusercontent.com/sparkssssssssss/epg/main/logo/黄金翡翠台.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=0737b75ee8906c00bb7bb8f666da72a0&key=15f515458cdb5107452f943a111cbe89'
    },
    'TVG': {
        'name': '黄金翡翠台',
        'license': '8fe3db1a24969694ae3447f26473eb9f:5cce95833568b9e322f17c61387b306f',
        'logo': 'https://github.com/sparkssssssssss/epg/blob/main/logo/%E9%BB%84%E9%87%91%E7%BF%A1%E7%BF%A0%E5%8F%B0.png?raw=true',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=8fe3db1a24969694ae3447f26473eb9f&key=5cce95833568b9e322f17c61387b306f'
    },
    'C': {
        'name': '无线新闻台',
        'license': '90a0bd01d9f6cbb39839cd9b68fc26bc:51546d1f2af0547f0e961995b60a32a1',
        'logo': 'https://raw.githubusercontent.com/wanglindl/TVlogo/main/img/TVB4.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=90a0bd01d9f6cbb39839cd9b68fc26bc&key=51546d1f2af0547f0e961995b60a32a1'
    },
    'CTVE': {
        'name': '娱乐新闻台',
        'license': '6fa0e47750b5e2fb6adf9b9a0ac431a3:a256220e6c2beaa82f4ca5fba4ec1f95',
        'logo': 'https://github.com/sparkssssssssss/epg/blob/main/logo/%E5%A8%B1%E4%B9%90%E6%96%B0%E9%97%BB%E5%8F%B0.png?raw=true',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=6fa0e47750b5e2fb6adf9b9a0ac431a3&key=a256220e6c2beaa82f4ca5fba4ec1f95'
    },
    'PCC': {
        'name': '凤凰卫视中文台',
        'license': '7bca0771ba9205edb5d467ce2fdf0162:eb19c7e3cea34dc90645e33f983b15ab',
        'logo': 'https://raw.githubusercontent.com/wanglindl/TVlogo/main/img/Phoenix1.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=7bca0771ba9205edb5d467ce2fdf0162&key=eb19c7e3cea34dc90645e33f983b15ab'
    },
    'PIN': {
        'name': '凤凰卫视资讯台',
        'license': '83f7d313adfc0a5b978b9efa0421ce25:ecdc8065a46287bfb58e9f765e4eec2b',
        'logo': 'https://raw.githubusercontent.com/wanglindl/TVlogo/main/img/Phoenix2.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=83f7d313adfc0a5b978b9efa0421ce25&key=ecdc8065a46287bfb58e9f765e4eec2b'
    },
    'PHK': {
        'name': '凤凰卫视香港台',
        'license': 'cde62e1056eb3615dab7a3efd83f5eb4:b8685fbecf772e64154630829cf330a3',
        'logo': 'https://raw.githubusercontent.com/wanglindl/TVlogo/main/img/Phoenix3.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=cde62e1056eb3615dab7a3efd83f5eb4&key=b8685fbecf772e64154630829cf330a3'
    },
    'EVT3': {
        'name': 'myTV SUPER 直播足球3台',
        'license': '84f456002b780253dab5534e9713323c:65aeb769264f41037cec607813e91bae',
        'logo': 'https://assets.livednow.com/logo/myTV-SUPER-Football-3.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=84f456002b780253dab5534e9713323c&key=65aeb769264f41037cec607813e91bae'
    },
    'EVT4': {
        'name': 'myTV SUPER 直播足球4台',
        'license': '848d6d82c14ffd12adf4a7b49afdc978:3221125831a2f980139c34b35def3b0d',
        'logo': 'https://assets.livednow.com/logo/myTV-SUPER-Football-4.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=848d6d82c14ffd12adf4a7b49afdc978&key=3221125831a2f980139c34b35def3b0d'
    },
    'EVT5': {
        'name': 'myTV SUPER 直播足球5台',
        'license': '54700d7a381b80ae395a312e03a9abeb:7c68d289628867bf691b42e90a50d349',
        'logo': 'https://assets.livednow.com/logo/myTV-SUPER-Football-5.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=54700d7a381b80ae395a312e03a9abeb&key=7c68d289628867bf691b42e90a50d349'
    },
    'EVT6': {
        'name': 'myTV SUPER 直播足球6台',
        'license': 'e069fc056280e4caa7d0ffb99024c05a:d3693103f232f28b4781bbc7e499c43a',
        'logo': 'https://assets.livednow.com/logo/myTV-SUPER-Football-6.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=e069fc056280e4caa7d0ffb99024c05a&key=d3693103f232f28b4781bbc7e499c43a'
    },
    'CCCM': {
        'name': '天映經典頻道',
        'license': '627b6ca150887912bec47ae4a9b85269:2bf49b2105d20544a6db89c0577b9802',
        'logo': 'https://assets.livednow.com/logo/天映經典頻道.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=627b6ca150887912bec47ae4a9b85269&key=2bf49b2105d20544a6db89c0577b9802'
    },
    'CMAM': {
        'name': '美亞電影台-HK',
        'license': 'c5d6f2afbd6b276312b0471a653828e1:ecbbb4a3ffa2200ae69058e20e71e91b',
        'logo': 'https://assets.livednow.com/logo/美亞電影台-HK.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=c5d6f2afbd6b276312b0471a653828e1&key=ecbbb4a3ffa2200ae69058e20e71e91b'
    },
    'EVT1': {
        'name': 'myTV SUPER直播足球1台',
        'license': 'e8ca7903e25450d85cb32b3057948522:d5db5c03608f5f6c8a382c6abcb829e4',
        'logo': 'https://raw.githubusercontent.com/sparkssssssssss/epg/main/logo/黄金翡翠台.png',
        'license_key': 'https://vercel-php-clearkey-hex-base64-json.vercel.app/api/results.php?keyid=e8ca7903e25450d85cb32b3057948522&key=d5db5c03608f5f6c8a382c6abcb829e4'
    }
}

def get_mytvsuper(channel):
    if channel not in CHANNEL_LIST:
        return '频道代号错误'

    api_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJib3NzX2lkIjoiMTM0MjIzNjUxIiwiZGV2aWNlX3Rva2VuIjoiaFpqc2lXY1BhVFpwRWE0WFh6S291SE5tIiwiZGV2aWNlX2lkIjoiTTJGbVlUQXlOV1l0T0RjMFlpMDBOelk0TFRrMFpEQXRNMkpoWkRrNE1qWmlOVFkyIiwiZGV2aWNlX3R5cGUiOiJ3ZWIiLCJkZXZpY2Vfb3MiOiJicm93c2VyIiwiZHJtX2lkIjoiTTJGbVlUQXlOV1l0T0RjMFlpMDBOelk0TFRrMFpEQXRNMkpoWkRrNE1qWmlOVFkyIiwiZXh0cmEiOnsicHJvZmlsZV9pZCI6MX0sImlhdCI6MTcxNjUyNzEzMCwiZXhwIjoxNzE2NTMwNzMwfQ.mqRRhl57KQRfNHxR_-Gox8dmj-is4mjAXYXiy-G4ShKVNgDMO2pjeteQj5hkJvuEt32SomRPp2Aj7Ok-MeTNpGbApedylG2R2h9ZrqTkFyYMxOt0u9O-qLzKCVRL7WJV-slf_co4n5QZyDeuv4BkwUUgj7TXt-cL1oNkIR3nbDyfp97fm9SHQbUjC-qAcIiDNjlTwbDgRK7PdVu7j3kkBiVAiuIHL9DVQ--hdMb-vkV-3yk1txfqdlv9Ulq5vmNwavN6xcW3zFisg_g0dBcUulbl1nglqf7lNhPj-dVTiOUfMLBMWjTLReBC_kc5RXlIizr8Q87y2ioYRIEEQss7nsiAInMI70KrZu9aEJbtyLo0I5t7XHlFh1G9CR2u_M512foanv4amsk75I925It2z5qLiZ83KuOLJXppOqX4D1cQQixmylT9MwJajnO21usMkTXDSXE2j2bSMaZ9dZ3eX8eZYxCdZkR5yxqQQKuHjKZsG-jiO02LmYCllNV9pfLNfcrMhXeG5jSHtTgpOiB2z-n5l3W_jw4F4B4xkB9U4QW-hneyUzgZTJb62qKrKiVdTL3-okaE0Yd572qucgw2SNZeqlIw5G0CWSRNMd7OS5MZbqJ4vO9B3hlTBxmM4bV1c30ewq54GKv5B0OVByKNxk0aVNKnZWt8Z25eofH9D_4"
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + api_token,
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Host': 'user-api.mytvsuper.com',
        'Origin': 'https://www.mytvsuper.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.15',
        'Referer': 'https://www.mytvsuper.com/',
        'X-Forwarded-For': '210.6.4.148'  # 香港原生IP  210.6.4.148
    }

    params = {
        'platform': 'android_tv',
        'network_code': channel
    }

    url = 'https://user-api.mytvsuper.com/v1/channel/checkout'
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return '请求失败'

    response_json = response.json()
    profiles = response_json.get('profiles', [])

    play_url = ''
    for profile in profiles:
        if profile.get('quality') == 'high':
            play_url = profile.get('streaming_path', '')
            break

    if not play_url:
        return '未找到播放地址'

    play_url = play_url.split('&p=')[0]

    license_key = CHANNEL_LIST[channel]['license_key']
    channel_name = CHANNEL_LIST[channel]['name']
    channel_logo = CHANNEL_LIST[channel]['logo']
    m3u_content = f"#EXTINF:-1 tvg-id=\"{channel}\" tvg-logo=\"{channel_logo}\",{channel_name}\n"
    m3u_content += "#KODIPROP:inputstream.adaptive.manifest_type=mpd\n"
    m3u_content += "#KODIPROP:inputstream.adaptive.license_type=clearkey\n"
    m3u_content += f"#KODIPROP:inputstream.adaptive.license_key={license_key}\n"
    m3u_content += f"{play_url}\n"

    return m3u_content

# 创建或打开文件用于写入
with open('mytvfree.m3u', 'w', encoding='utf-8') as m3u_file:
    # 写入 M3U 文件的头部
    m3u_file.write("#EXTM3U\n")

    # 遍历所有频道并写入每个频道的 M3U 内容
    for channel_code in CHANNEL_LIST.keys():
        m3u_content = get_mytvsuper(channel_code)
        m3u_file.write(m3u_content)

print("所有频道的 M3U 播放列表已生成并保存为 'mytvfree.m3u'。")
