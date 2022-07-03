import requests
from bs4 import BeautifulSoup

url = "https://testselect.uuboyscy.repl.co/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

inputObjList = soup.select('input')
for i in inputObjList:
    print(i)

for i in inputObjList:
    if i['type'] == 'hidden':
        print(i['name'], i['value'])