import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

for i in range(0, 5):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    titles = soup.select('div.title')
    # print(titles)
    for title in titles:
        # print(title)
        titleObj = title.select_one('a')  # a-tag object -> <a href="/bbs/movie/M.1656691282.A.EC0.html">[新聞] 為何59歲阿湯哥能輾壓恐龍？ 全台票房</a>
        try:
            titleName = titleObj.text
            titleUrl = "https://www.ptt.cc" + titleObj["href"]
            print(titleName)
            print(titleUrl)
        except AttributeError as e:
            print(title)
        print("======")

    lastPageUrl = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]['href']
    lastPageUrl = "https://www.ptt.cc" + soup.select('a.btn.wide')[1]['href']
    url = lastPageUrl
    # print(lastPageUrl)