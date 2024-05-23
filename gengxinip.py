addEventListener("fetch", event => {
  event.respondWith(handleRequest(event.request))
})

const api_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJib3NzX2lkIjoiMTM0MjIzNjUxIiwiZGV2aWNlX3Rva2VuIjoiQTdMN212VjJFREgzOGtZbzl2dVdQdTJFIiwiZGV2aWNlX2lkIjoiTnpZMlpqY3hPVEl0WkdJMk5pMDBOVFkyTFRneVkyUXRNall3WkdGaE5tSm1NV1EzIiwiZGV2aWNlX3R5cGUiOiJ3ZWIiLCJkZXZpY2Vfb3MiOiJicm93c2VyIiwiZHJtX2lkIjoiTnpZMlpqY3hPVEl0WkdJMk5pMDBOVFkyTFRneVkyUXRNall3WkdGaE5tSm1NV1EzIiwiZXh0cmEiOnsicHJvZmlsZV9pZCI6MX0sImlhdCI6MTcxNjQ2MzQ5NCwiZXhwIjoxNzE2NDY3MDk0fQ.EiwCYPH3a6tRpHkO2cOe4bwd4jPVkWmbyjNqSLU5P3FY7YzWhunag8TQYGfwlx8VjVqYkZf8fXK3sqw3AVwzybPWPT13svVgVj7g5QF48TArIIymgC_sgaoYOMv4VAErHYBTQHdRIwPqB82jbqpMH333gwREeiiqmqa6RAhWtLzuFqZsXXXbfNtOL7kXp7M-HWQTCsZRI52DJNVfH-SW4F5j83FzF8CEEgL15a1C7Tk-ute0iBjueay72v67xWlbN8ltRICZdOvWMwapoAY8v1hAn202muuWM_xNmeJN9zT3qWjFA6nGS6gSZNFVTenL_35hBz1O9QRLD9PnRZCxJJ6ypUp4Ts1Oi_36PGYd6WDYYhWEqYsDapDILt0iRMLJpXHg1M-VGzX4z1RRqhSt5fwLvY1Gizjb0y6i9ojtmgbSb5xsfOe6kPh9ipazmnOUQ9ENh98iNPRoQszBHT1D6ZQ6qKKiCx_o99rpWTdJfFXzZsmdWgopcxnPI6U6d9MxcbcOx5tRDTQXyUqtnsNxKk1sedgWTN1yR26-HsPVsMYJ4Bl5q74A8bh-6S2M6-b0vrQ-UiEMHhumZTRGCwxXS-dFJGocFeOpjSRuLed286CLUuMigoIhr9dWoP8tID4PIrRGWwU7a-C0ea_SO_9KXhXeZlny1S0pylegdo8uuuo';
async function get_mytvsuper(channel) {
  const headers = {
    'Accept': 'application/json',
    'Authorization': `Bearer ${api_token}`,
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Host': 'user-api.mytvsuper.com',
    'Origin': 'https://www.mytvsuper.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.15',
    'Referer': 'https://www.mytvsuper.com/',
    'X-Forwarded-For': '210.6.4.148', 
  }

  const params = new URLSearchParams();
  params.append('platform', 'android_tv');
  params.append('network_code', channel);

  const response = await fetch(`https://user-api.mytvsuper.com/v1/channel/checkout?${params}`, { headers });
  if (response.status != 200) {
    return null;
  }

  const json = await response.json();
  const profiles = json.profiles || [];
  let play_url = '';
  for (let i of profiles) {
    if (i.quality === 'high') {
      play_url = i.streaming_path;
      break;
    }
  }

  if (!play_url) {
    return null;
  }
  return play_url.split('&p=')[0];
}

async function handleRequest(request) {
  const url = new URL(request.url);
  const path = url.pathname.split('/');
  const id = path.pop();

  const redirect_url = await get_mytvsuper(id) || 'https://nolive.livednow.com/nolive.m3u8';

  let cacheControl = 'public, max-age=10'
  if (redirect_url !== 'https://nolive.livednow.com/nolive.m3u8') {
    cacheControl = 'public, max-age=43200' 
  }

  const response = new Response(null, {
    status: 302,
    headers: {
      Location: redirect_url,
      'Cache-Control': cacheControl,
    },
  });
  return response;
}
