import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/M.1656606609.A.E9B.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

articleObj = soup.select_one('div[id="main-content"]')

# print(articleObj)
for div in articleObj.select('div'):
    # print(div)
    # print(div.extract())
    div.extract()

for div in articleObj.select('span'):
    div.extract()

print(articleObj.text)