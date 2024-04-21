import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://www.aliexpress.com',
    'priority': 'u=1, i',
    'referer': 'https://www.aliexpress.com/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36',
}


params = {
    'productId': '1005006438619019',
    'lang': 'en_US',
    'country': 'DZ',
    'page': '1',
    'pageSize': '10',
    'filter': 'all',
    'sort': 'complex_default',
}

response = requests.get('https://feedback.aliexpress.com/pc/searchEvaluation.do', params=params, headers=headers)
print(response.status_code)

data = response.json()
print(data['data']['evaViewList'][1]["buyerName"])

