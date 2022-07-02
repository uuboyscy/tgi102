from urllib import request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url = "https://www.ptt.cc/bbs/joke/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

# res = request.urlopen(url=url)
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

# print(res.read().decode('utf8'))
htmlStr = res.read().decode('utf8')
soup = BeautifulSoup(htmlStr, "html.parser")
# soup = BeautifulSoup(htmlStr, "lxml")
print(soup)
