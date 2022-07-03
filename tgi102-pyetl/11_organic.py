import requests
from bs4 import BeautifulSoup

url = "https://organic.afa.gov.tw/InOrganic/QueryApplyList"


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

data = {
    "TYPE": "1",
    "YEAR": "111",
    "qNnify_NO": "",
    "qC_NAME": "",
    "qPaper_NO": "",
    "qProduct_NAME": "米".encode("big5"),
    "B": "查　　詢"
}

res = requests.post(url, headers=headers, data=data)
# print(res.text)

headersStr = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 91
Content-Type: application/x-www-form-urlencoded
Cookie: JSESSIONID=198A8D0A04500D2CA1841A5233CB620F; TS018193af=010df39fec514c83f57c42616e95334ffc2c4de1cf31579ff68cc8b57939c5c6f690bc623411507dc0ed04b1a0371814a5c98dea7709faf9c8e65e4b1729696539581dd461; _ga=GA1.3.1459203624.1655739571; TS01bc7d78=010df39fec04d6e14fd2dccc737fc877a3f66b41dad7b7c383cd15d0dc9d24b5d02640623fed1be348dd7b0bbc4eddd1f1b60af536
Host: organic.afa.gov.tw
Origin: https://organic.afa.gov.tw
Referer: https://organic.afa.gov.tw/InOrganic/QueryApplyList
sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"""

headers = {r.split(": ")[0]: r.split(": ")[1] for r in headersStr.split("\n")}
print(headers)