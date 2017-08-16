import requests
url = 'http://www.10086.cn/zj/index_571_571.html'
html = requests.get(url)

print(html.text)